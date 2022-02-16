import adminapp.views as adminapp
from django.urls import path, re_path

app_name = 'adminapp'

urlpatterns = [

    re_path(r'^users/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^users/read/$', adminapp.UsersListView.as_view(), name='users'),
    re_path(r'^users/update/(?P<pk>\d+)$', adminapp.user_update, name='user_update'),
    re_path(r'^users/delete/(?P<pk>\d+)$', adminapp.user_delete, name='user_delete'),
    
    path('categories/create/',  adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:pk>', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    re_path(r'^categories/delete/(?P<pk>\d+)$', adminapp.category_delete, name='category_delete'),

    path('products/create/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),
]
