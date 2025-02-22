# OAuth_Server

NextJS frontend webapp queries this microservice(OAuth) before querying any
other microservice, to verify if user can access said microservice data.

CORS: only nextjs app can make requests to OAuth and other microservices,
nextjs SHALL NEVER be used as a proxy to microservices.
Except under local development(i.e., `localhost`||`127.0.0.1`) CORS will block
Postman, curl, wget, or any other requests that do not originate from the nextjs
frontend app.

## Folder structure

<!-- TODO: Folder Structure under review as more changes might be required -->

``` txt
OAuth/
├── .github/
│   ├── workflows/
├── .gitignore
├── .oauth.env
├── .oauth.env.example
├── .pylintrc
├── manage.py
├── Dockerfile
├── requirements.txt
├── venv
├── README.md
├── api
│   ├── __init__.py
│   ├── auth_n_auth/
│     ├── __init__.py
│     ├── models/
│     ├── views/
│     ├── migratrions/
│     ├── apps.py
│     ├── admin.py
│     ├── urls.py
│   ├── jwt_mngmt/
│   ├── mfa_mngmt/
│   ├── user_preferences/
├── config
└── logs
```

## Pylint

Setting up pylint:

1. `pip install pylint pylint-django`
2. Install **Pylint** and **isort** vscode extensions
3. Set Python Interpreter to `./venv/bin/python`

## Local Postgresql

`source venv/bin/activate`
`python manage.py makemigrations`
`python manage.py migrate`

### Setting Postgresql to UTC

<https://stackoverflow.com/questions/6663765/postgres-default-timezone>
`ALTER DATABASE postgres SET timezone TO 'GMT';`
`ALTER DATABASE quickqr_dev SET timezone TO 'GMT';`

<https://stackoverflow.com/questions/35884639/can-we-have-django-datetimefield-without-timezone>
in `/home/konstantin/quickQr/_OAuth/config/settings.py` set `USE_TZ = False`

## Permissions

We have roles, services and url based permissions.

subscription is used to determine which services are available to users.
all services are available to admins and account owners.

account owners have permissions to all services available within subscription
and these permissions cannot be altered.

There are 2 default roles: account-owner, admin.
Next there are service-only roles, i.e. accounting, etc.
More roles can be created.
All roles except account-owner and admin can be edited.
Roles are soft deleted, and can be disabled.

when a subscription is purchased, the email through which the purchase is made
is used to create the first and only account with an account-owner role.
Once all dbs, caches, domain prefixes, and microservices are deployed and seeded
they are the only user that can sign in.
the account owner can create sitting and non-sitting users, sitting users take
up seats. The total number of seats is determined by the subscription and
extra seats can be purchased by the account owner.

the only difference between account-owner and admin is that the account-owner
can manage the subscription whereas admin cannot. The roles are not editable,
i.e., their permissions cannot be changed, they have access to all services and
all pages within said services.

---

in redis we have the following keys:

* `registered-services`
* `subscription-services`
* `role:<role-id>:services`
* `role:<role-id>:service:<service-id>:permissions`

we get the user role(role_id | name) from jwt generated on login, and passed to
views by middleware.

`registered-services` and `subscription-services` are seeded from
api/auth_n_auth/models/services.py
We need both so that we can display non-subscription services to users when they
login to entice them to upgrade their subscription.


-you do the redis-cli to get it active and then you can view by KEYS *