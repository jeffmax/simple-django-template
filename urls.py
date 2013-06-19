import re
from django.conf import settings
from django.conf.urls.defaults import patterns, url
from views import main

urlpatterns = patterns('', (r'^$', main))

# In production, these two locations must be served up statically
urlpatterns += patterns('django.views.static',
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), 'serve', {
        'document_root': settings.MEDIA_ROOT
    }),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), 'serve', {
        'document_root': settings.STATIC_ROOT
    }),
)

