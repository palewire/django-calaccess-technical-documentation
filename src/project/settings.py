import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_DIR = os.path.join(BASE_DIR, os.pardir)
SECRET_KEY = 'd7lg-3a2yc6t3anqr!rhhcd)u!a^-j9r4o7j5_@yibmmuz55h3'

DEBUG = False
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]
STATIC_ROOT = os.path.join(BASE_DIR, ".static")
MEDIA_ROOT = os.path.join(BASE_DIR, ".media")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'calaccess_raw',
    'toolbox',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {}
CALACCESS_DAT_SOURCE = ''
CALACCESS_STORE_ARCHIVE = False

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
