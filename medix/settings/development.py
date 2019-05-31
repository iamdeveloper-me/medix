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

DEFAULT_FROM_EMAIL = 'aarti@mailinator.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587

ROOT_URL = 'http://localhost:8000'

# local settings
try:
    from .local import *
except ImportError:
    pass