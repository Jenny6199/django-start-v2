from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainapp.models import ProductCategory, Product
import random
from django.conf import settings
from django.core.cache import cache


def get_hot_product():
    products_all = Product.objects.all().select_related('category')
    return random.sample(list(products_all), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(
        category=hot_product.category
    ).select_related(
        'category'
    ).exclude(pk=hot_product.pk)[:3]
    return same_products


def main(request):
    title = 'главная'

    products_all = Product.objects.filter(
        is_active=True,
        category__is_active=True).select_related('category')[:3]

    content = {
        'title': title,
        'products': products_all,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    our_products = Product.objects.all()

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все',
            }
            our_products = Product.objects.filter(
                is_active=True,
                category__is_active=True,
            ).select_related().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            our_products = Product.objects.filter(
                category__pk=pk,
                is_active=True,
                category__is_active=True,
            ).select_related().order_by('price')

        paginator = Paginator(our_products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_products': hot_product,
        'same_products': same_products,
        'products': our_products,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all().select_related(),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/product.html', content)


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name +'.json'), 'r', errors='ignore') as infile:
        return json.load(infile)


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product():
    if settings.LOW_CACHE:
        key = 'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)

