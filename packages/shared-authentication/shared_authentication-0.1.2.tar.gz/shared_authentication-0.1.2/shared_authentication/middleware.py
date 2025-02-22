from django.utils.deprecation import MiddlewareMixin
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView
from .authentication import JWECustomAuth, JWEAndMFACustomAuth

class CustomAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Create a dummy view to use the authentication and permission classes
        view = APIView()
        view.authentication_classes = [JWECustomAuth, JWEAndMFACustomAuth]
        view.permission_classes = [IsAuthenticated]

        # Create a DRF request object
        drf_request = Request(request)

        # Authenticate the request
        for auth_class in view.authentication_classes:
            auth_instance = auth_class()
            user_auth_tuple = auth_instance.authenticate(drf_request)
            if user_auth_tuple is not None:
                request.user, request.auth = user_auth_tuple
                break
        else:
            raise AuthenticationFailed('Authentication credentials were not provided.')

        # Check permissions
        for permission_class in view.permission_classes:
            permission_instance = permission_class()
            if not permission_instance.has_permission(drf_request, view):
                raise AuthenticationFailed('Permission denied.')