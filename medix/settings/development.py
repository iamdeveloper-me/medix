from .base import *

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
STATICFILES_DIRS = (
    PROJECT_APPS.child("static"),
)

MEDIA_ROOT = PROJECT_APPS.child("media")
MEDIA_URL = '/media/'

DEFAULT_FROM_EMAIL = 'anmol.thoughtwin@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587

ROOT_URL = 'http://18.218.141.80'
# local settings
try:
    from .local import *
except ImportError:
    pass