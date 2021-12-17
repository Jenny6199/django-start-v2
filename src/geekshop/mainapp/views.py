from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404


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


    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'linsk_menu': links_menu,
            'category': category,
            'products': products,
            'small_images': small_images,
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'small_images': small_images,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')
