from .base import *


DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'd3',
		'USER': environ['DB_USERNAME'],
		'PASSWORD': environ['DB_PASSWORD'],
		'HOST': 'localhost',
		'PORT': '',
	}
}

STATIC_URL = '/assets/'

INSTALLED_APPS += ()