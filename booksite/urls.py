from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
# urls.py #
from booksite import settings

urlpatterns = patterns('',
   
    #map to insert to the db
    url(r'^insert_author/$','book.views.insert_author'),
    url(r'^insert_book/$','book.views.insert_book'),

    #map to return the insert GUI HTML
    url(r'^/$','book.views.index'),
    url(r'^$','book.views.index'),
    url(r'^index/$','book.views.index'),
    url(r'^add_author/$','book.views.add_author'),
    url(r'^add_book/$','book.views.add_book'),
    url(r'^view_book/$','book.views.view_book'),
    url(r'^search_author/$','book.views.search_author'),
    #map to view items 
    url(r'^view_author/$','book.views.view_author'),
    url(r'^view_book/$','book.views.view_book'),

    #search
    url(r'^search_by_author/$','book.views.search_by_author'),
    url(r'^search_book/$','book.views.search_book'),

    url(r'^admin/', include(admin.site.urls)),
    #delete and update
    url(r'^delete/$','book.views.delete_book'),
    url(r'^update_book/$','book.views.update_book'),
    url(r'^update/$','book.views.update'),
    #match media
    (r'^Media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS,'show_indexes': True}),

    '''
    url(r'^Media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),
    
    '''
)
