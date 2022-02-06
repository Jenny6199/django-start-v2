from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainapp.models import ProductCategory, Product
import random


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
    our_products = Product.objects.all().select_related('category')

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все',
            }
            our_products = Product.objects.filter(
                is_active=True,
                category__is_active=True,
            ).select_relaged('product').order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            our_products = Product.objects.filter(
                category__pk=pk,
                is_active=True,
                category__is_active=True,
            ).select_related('product').order_by('price')

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
        'links_menu': ProductCategory.objects.all().select_related('category'),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/product.html', content)
