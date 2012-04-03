from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from core.views import homepage
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', homepage,{'template':'index.html'}),
    url(r'^inscricao/', include('subscriptions.urls', namespace='subscriptions')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^categoria/', include('categoria.urls', namespace='categoria')),
    (r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += staticfiles_urlpatterns()