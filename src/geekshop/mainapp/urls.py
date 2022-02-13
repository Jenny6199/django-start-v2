from django.urls import path, re_path
import mainapp.views as mainapp
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    # This urlpatterns is used def path:
    # path('', mainapp.products, name='index'),
    # path('category/<int:pk>/', mainapp.products, name='category'),
    # path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),
    # path('product/<int:pk>/', mainapp.product, name='product'),

    # This urlpatterns is used def re_path
    re_path(r'^$', mainapp.products, name='index'),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
    re_path(r'^category/(?P<pk>\d+)/$', cache_page(3600)(mainapp.products), name='category'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),
    # This block for use cache with ajax
    re_path(r'^category/(?P<pk>\d)/ajax/$', cache_page(3600)(mainapp.products_ajax)),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$', cache_page(3600)(mainapp.products_ajax)),
]
