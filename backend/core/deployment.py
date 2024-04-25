import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = ['*']

# CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME'],]

DEBUG = False

SECRET_KEY = os.getenv('MY_SECRET_KEY')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000'
# ]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
# CONNECTION_STR = {pair.split('-')[0]:pair.split('-')[1] for pair in CONNECTION.split(' ')}

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':os.getenv('DB_NAME'),
        'USER':os.getenv('DB_USER'),
        'PASSWORD':os.getenv('DB_PASSWORD'),
        'HOST':os.getenv('DB_HOST'),
        'PORT':'5432',
    }
}

STATIC_ROOT = BASE_DIR/'staticfiles'