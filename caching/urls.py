from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^persite_page$', 'caching.views.persite_page', name='persite_page'),
    url(r'^nocache$', 'caching.views.nocache', name='nocache'),
    url(r'^perview_page$', 'caching.views.perview_page', name='perview_page'),
    url(r'^admin/', include(admin.site.urls)),
)
