from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]

    content = {
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)

    title = 'продукты'

    related_products = [
        {'href': '#', 'image': 'img/product-11.jpg'},
        {'href': '#', 'image': 'img/product-21.jpg'},
        {'href': '#', 'image': 'img/product-31.jpg'},
    ]

    small_images = [
        {'href': '#', 'image': 'img/controll.jpg'},
        {'href': '#', 'image': 'img/controll1.jpg'},
        {'href': '#', 'image': 'img/controll2.jpg'},
    ]

    categories_menu = []

    categories = ProductCategory.objects.all()
    for item in categories:
        category_info = {'href': 'empty', 'name': item.name}
        categories_menu.append(category_info)

    content = {
        'title': title,
        'related_products': related_products,
        'small_images': small_images,
        'links_menu': categories_menu,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')
