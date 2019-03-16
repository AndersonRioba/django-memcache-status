import os
import sys

DEBUG = True

TESTAPP_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'testsecretkey'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TESTAPP_DIR, 'testdb.sqlite'),
    }
}

STATIC_ROOT = os.path.join(TESTAPP_DIR, '.static')
MEDIA_ROOT = os.path.join(TESTAPP_DIR, '.uploads')

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

ROOT_URLCONF = 'memcache_status.tests.testapp.urls'

INSTALLED_APPS = [
    'memcache_status',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]

if os.getenv('TEST_WITH_DEBUGTOOLBAR', False) == 'on':
    sys.stdout.write('Testing with django-debug-toolbar support.\n')
    INSTALLED_APPS.insert(0, 'debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1']