from django.urls import path, re_path
import mainapp.views as mainapp
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    # path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),
    # path('product/<int:pk>/', mainapp.product, name='product'),

    re_path(r'^$', mainapp.products, name='index'),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
    re_path(r'^category/(?P<pk>\d)/ajax/$', cache_page(3600)(mainapp.products_ajax)),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$', cache_page(3600)(mainapp.products_ajax)),

    # it need to restore - dont work with product/category/0/ No ProductCategory matches the given query.
    # re_path(r'^category/(?P<pk>\d+)/$', cache_page(240)(mainapp.products), name='category'),

    # It need to restore - dont maches query. Why, I dont know
    # re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),
]
