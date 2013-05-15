import os
import sys
from django.conf.urls.defaults import patterns
from django.http import HttpResponse

filepath, extension = os.path.splitext(os.path.abspath(__file__))

ROOT_URLCONF = os.path.basename(filepath)

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'testdb'
    }
}

DEBUG = True

SECRET_KEY = "PUT_SOMETHING_REAL_HERE"

INSTALLED_APPS = (os.path.split(os.path.dirname(os.path.abspath(__file__)))[-1],)

def view (request):
   return HttpResponse("OK")

urlpatterns = patterns('', (r'^$', view))
