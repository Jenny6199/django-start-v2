from django.urls import path, re_path
import mainapp.views as mainapp
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    # path('', mainapp.products, name='index'),
    path('category/<int:pk>/', cache_page(240)(mainapp.products), name='category'),
    # path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),
    # path('product/<int:pk>/', mainapp.product, name='product'),

    re_path(r'^$', mainapp.products, name='index'),
    # re_path(r'category/(?P<pk>\d+)/', mainapp.products, name='category'),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),
]
