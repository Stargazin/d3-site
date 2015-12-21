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


# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.postgresql_psycopg2',
# 		'NAME': 'd3',
# 		'USER': 'd3',
# 		'PASSWORD': 'd3',
# 		'HOST': 'localhost',
# 		'PORT': '',
# 	}
# }

STATIC_URL = '/assets/'

INSTALLED_APPS += ()