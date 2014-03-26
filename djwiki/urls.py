from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'core.views.index', name='wiki_index'),
    url(r'^(?P<page_url>\w+)$', 'core.views.view', name='view_page'),
    url(r'^(?P<page_url>\w+)/edit/$', 'core.views.edit', name='edit_page'),

    # Admin site urls.
    url(r'^admin/', include(admin.site.urls)),
)
