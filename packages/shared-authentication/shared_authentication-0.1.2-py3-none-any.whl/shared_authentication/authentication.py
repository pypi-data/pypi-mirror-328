import json
from datetime import datetime, timezone
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api.authentication.helpers import decrypt_data
from api.redis import keys as redis_keys
from api.redis.client import RedisClient
from api.utils.token import extract_claims_from_jwt, extract_jwt_from_jwe

redis = RedisClient()
client = redis.get_client(settings.REDIS_DB_NAME)

class JWECustomAuth(BaseAuthentication):
    def authenticate(self, request):
        try:
            authorization = request.META.get('HTTP_AUTHORIZATION')
        except Exception as e:
            raise AuthenticationFailed(f'Missing Authorization header: {e}') from e

        if authorization is None or not authorization.startswith('Bearer '):
            raise AuthenticationFailed('Invalid Authorization header.')

        token = authorization.split(' ')[1]

        encrypted_token = client.get(redis_keys.blacklist_jwe(token))
        if encrypted_token is not None:
            raise AuthenticationFailed('Blacklisted refresh token')

        try:
            decrypted_token = decrypt_data(token)
            jwt_token = extract_jwt_from_jwe(decrypted_token)
            jwt_data = extract_claims_from_jwt(jwt_token)
        except Exception as e:
            raise AuthenticationFailed(f'Invalid token: {e}') from e

        exp = jwt_data.get('exp')
        if exp is None:
            raise AuthenticationFailed('Invalid Authorization token.')
        time_diff = datetime.now(timezone.utc) - datetime.fromisoformat(exp)

        if time_diff.total_seconds() > settings.AUTH_TTL:
            raise AuthenticationFailed('Authorization expired, must login.')

        user = json.loads(jwt_data['values'])
        return (user, None)

class JWEAndMFACustomAuth(BaseAuthentication):
    """
    Custom authentication class to verify JWT tokens and MFA.
    """
    def authenticate(self, request):
        try:
            authorization = request.META.get('HTTP_AUTHORIZATION')
        except Exception as e:
            raise AuthenticationFailed(f'Missing Authorization header: {e}') from e

        if authorization is None or not authorization.startswith('Bearer '):
            raise AuthenticationFailed('Invalid Authorization header.')

        token = authorization.split(' ')[1]

        try:
            decrypted_token = decrypt_data(token)
            jwt_token = extract_jwt_from_jwe(decrypted_token)
            jwt_data = extract_claims_from_jwt(jwt_token)
        except Exception as e:
            raise AuthenticationFailed(f'Invalid token: {e}') from e

        exp = jwt_data.get('exp')
        if exp is None:
            raise AuthenticationFailed('Invalid Authorization token.')
        time_diff = datetime.now(timezone.utc) - datetime.fromisoformat(exp)

        if time_diff.total_seconds() > settings.AUTH_TTL:
            raise AuthenticationFailed('Authorization expired, must login.')

        user = json.loads(jwt_data['values'])
        mfa_key = redis_keys.token_mfa_key(user['id'], token)
        blacklist_key = redis_keys.blacklist_jwe(token)

        try:
            pipe = client.pipeline()
            pipe.get(mfa_key)
            pipe.get(blacklist_key)
            mfa_keys, blacklist_keys = pipe.execute()
        except Exception as e:
            msg = 'Internal Server Error, could not connect to redis.'
            raise AuthenticationFailed(msg) from e

        if mfa_keys:
            raise AuthenticationFailed('MFA validation required.')

        if blacklist_keys:
            raise AuthenticationFailed('Blacklisted token. New Login required.')

        user['authorization'] = token
        user['authorization_expiry'] = exp
        return (user, None)