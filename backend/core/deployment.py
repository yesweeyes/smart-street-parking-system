import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = ['*']

load_dotenv()

STATIC_ROOT = BASE_DIR/'staticfiles'

CSRF_TRUSTED_ORIGINS = ['*']

DEBUG = False

SECRET_KEY = os.getenv('MY_SECRET_KEY')

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True


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
