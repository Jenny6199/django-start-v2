from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', 'is_staff', username)

    content = {
        'title': title,
        'objects': users_list,
    }

    return render(request, 'adminapp/users.html', content)


def user_create(request):
    pass


def user_update(request):
    pass


def user_delete(request):
    pass


