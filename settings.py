import os
import sys

filepath, extension = os.path.splitext(os.path.abspath(__file__))

ROOT_URLCONF = '{{ PROJECT_NAME.urls }}'

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'testdb'
    }
}

DEBUG = True

SECRET_KEY = "PUT_SOMETHING_REAL_HERE"

INSTALLED_APPS = (os.path.split(os.path.dirname(os.path.abspath(__file__)))[-1],
                  'django.contrib.staticfiles',)
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.csrf',)
MIDDLEWARE_CLASSES = ('django.middleware.csrf.CsrfViewMiddleware',)

FORCE_SCRIPT_NAME = ""

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, '_site/media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, '_site/static')
STATIC_URL = FORCE_SCRIPT_NAME+"/static/"

MEDIA_URL = FORCE_SCRIPT_NAME+"/media/"

