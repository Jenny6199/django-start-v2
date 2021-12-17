from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

url_patterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>)/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>', basketapp.basket_remove, name='remove'),
]
