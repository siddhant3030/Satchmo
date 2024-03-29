# this is an extremely simple Satchmo standalone store.

import logging
import os, os.path

LOCAL_DEV = True
DEBUG = True

if LOCAL_DEV:
    INTERNAL_IPS = ('127.0.0.1',)

DIRNAME = os.path.dirname(os.path.abspath(__file__))

SATCHMO_DIRNAME = DIRNAME

gettext_noop = lambda s:s

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
   ('en', gettext_noop('English')),
)

ROOT_URLCONF = 'localsite.urls'

#These are used when loading the test data
SITE_NAME = "mystore"

DATABASES = {
    'default': {
        # The last part of ENGINE is 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'ado_mssql'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DIRNAME, 'mystore.db'),  # Or path to database file if using sqlite3
        #'USER': '',             # Not used with sqlite3.
        #'PASSWORD': '',         # Not used with sqlite3.
        'HOST': '',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',             # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = '@dd$j3#u8b#m9ox#a#k2ile%kjd))r+xy((k*x3f0kdib#6l%u'

DATABASES['default']['OPTIONS'] = {
   'init_command' : 'SET NAMES "utf8"',
   }

##### For Email ########
# If this isn't set in your settings file, you can set these here
#EMAIL_HOST = 'host here'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'your user here'
#EMAIL_HOST_PASSWORD = 'your password'
#EMAIL_USE_TLS = True

#These are used when loading the test data
SITE_DOMAIN = "localhost"
SITE_NAME = "Simple Satchmo"

# not suitable for deployment, for testing only, for deployment strongly consider memcached.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'satchmo-cache',
        'TIMEOUT': 60
    }
}
ACCOUNT_ACTIVATION_DAYS = 7

#Configure logging
LOGFILE = "satchmo.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(DIRNAME,LOGFILE),
                    filemode='w')

logging.getLogger('django.db.backends').setLevel(logging.INFO)
logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.getLogger('l10n').setLevel(logging.INFO)
logging.getLogger('suds').setLevel(logging.INFO)
logging.info("Satchmo Started")