from .views import *
from django.urls import path, include


urlpatterns = [
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
         product_info,
         name='product_info'),
    path(r'^$', show_product_list, name='show_product_list'),
    path(r'^(?P<category_slug>[-\w]+)/$',
         show_product_list,
         name='show_product_list_by_category'),
]