from django.shortcuts import render


def index(request):
    content = dict()
    return render(request, 'mainapp/index.html', content)


def category(request):
    content = dict()
    return render(request, 'mainapp/category.html', content)


def single_product(request):
    content = dict()
    return render(request, 'mainapp/single-product.html', content)
