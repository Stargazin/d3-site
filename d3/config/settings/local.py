from .base import *


DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'd3',
		'USER': 'd3',
		'PASSWORD': 'd3',
		'HOST': 'localhost',
		'PORT': '',
	}
}

INSTALLED_APPS += ()