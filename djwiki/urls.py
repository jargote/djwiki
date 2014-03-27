from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # Page Views
    url(r'^$', 'core.views.index', name='wiki_index'),
    url(r'^wiki/(?P<page_url>[a-zA-Z0-9_/]+)/$', 'core.views.view_page',
        name='view_page'),
    url(r'^wiki(?P<page_url>[a-zA-Z0-9_/]+)/edit/$', 'core.views.edit_page',
        name='edit_page'),

    # Change log views
    url(r'^changelog/$', 'core.views.changelog', name='global_changelog'),
    url(r'^changelog/(?P<page_url>[a-zA-Z0-9_/]+)/$',
        'core.views.changelog', name='changelog'),

    # Admin site urls.
    url(r'^admin/', include(admin.site.urls)),
)
