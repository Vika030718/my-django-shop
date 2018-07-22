from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.product, name='product'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^search/(?P<category_id>[0-9]+)/$', views.search, name='search'),
     url(r'^favorites/$', views.favorites, name='favorites'),
]
