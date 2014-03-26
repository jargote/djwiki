from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # Change log views
    url(r'^changelog/$', 'core.views.changelog', name='global_changelog'),

    # Page Views
    url(r'^$', 'core.views.index', name='wiki_index'),
    url(r'^(?P<page_url>\w+)/$', 'core.views.view_page', name='view_page'),
    url(r'^(?P<page_url>\w+)/edit/$', 'core.views.edit_page', name='edit_page'),
    url(r'^(?P<page_url>\w+)/changelog/$', 'core.views.changelog',
        name='changelog'),

    # Admin site urls.
    url(r'^admin/', include(admin.site.urls)),
)
