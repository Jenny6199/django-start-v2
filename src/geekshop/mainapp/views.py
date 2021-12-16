from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):

    title = 'продукты'

    related_products = [
        {'href': '#', 'image': 'img/product-11.jpg'},
        {'href': '#', 'image': 'img/product-21.jpg'},
        {'href': '#', 'image': 'img/product-31.jpg'},
    ]

    content = {
        'title': title,
        'related_products': related_products,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')
