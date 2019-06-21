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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'


DEFAULT_FROM_EMAIL = 'vinod.dangi@thoughtwin.com'
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