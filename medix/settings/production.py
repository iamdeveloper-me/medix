from .base import *
import os,sys

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     'medix',
        'USER':     'postgres',
        'PASSWORD': 'psql',
        'HOST':     'localhost',
        'PORT':     5432,
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_DIR.child("collected_static")
STATICFILES_DIRS = (
    PROJECT_APPS.child("static"),
)

MEDIA_ROOT = PROJECT_APPS.child("media")
MEDIA_URL = '/media/'

DEFAULT_FROM_EMAIL = 'preetamthoughtwin@mailinator.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587

ROOT_URL = "http://18.218.141.80"