from re import escape

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', direct_to_template, { 'template': 'home.html' }, 'homepage'),
	(r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^%s/(.*)$' % escape(settings.MEDIA_URL.strip('/')), 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
	)
