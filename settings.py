import os
import sys
from django.conf.urls.defaults import patterns
from django.http import HttpResponse
filepath, extension = os.path.splitext(__file__)

ROOT_URLCONF = os.path.basename(filepath)
sys.path.append("..")

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'testdb'
    }
}


INSTALLED_APPS = (os.path.basename(filepath),)

def view (request):
   return HttpResponse("HI!")

urlpatterns = patterns('', (r'^$', view))


