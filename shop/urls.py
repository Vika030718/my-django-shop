from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.product, name='product'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^search/(?P<category_id>[0-9]+)/$', views.search, name='search'),
    url(r'^favorites/$', views.favorites, name='favorites'),
    url(r'^add_to_favorites/(?P<product_id>[0-9]+)/$',
        views.add_to_favorites,
        name='add_to_favorites'),
    url(r'^remove_from_favorites/(?P<product_id>[0-9]+)/$',
        views.remove_from_favorites,
        name='remove_from_favorites'),
    url(r'^send_email/$', views.send_email, name='send_email'),
]
