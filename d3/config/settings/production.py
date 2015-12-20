from .base import *


DEBUG = False

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

ALLOWED_HOSTS = [
	'.diablo3-items.com',
	'45.55.67.133'
	]


STATIC_URL = '/static/'

#static_root is where collectstatic pulls everything
STATIC_ROOT = BASE_DIR.parent.child("staticfiles")

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'DENY'

INSTALLED_APPS += ()