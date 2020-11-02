import os
import json
from django.shortcuts import render
from karma.settings import BASE_DIR


DATA_DIR = os.path.join(BASE_DIR, 'data', 'mainapp')


def get_related_products() -> dict:
    with open(os.path.join(DATA_DIR, 'related_products.json')) as f:
        related_products_data = json.load(f)
    related_products = related_products_data.get("related_products") or dict()
    return related_products


def index(request):
    with open(os.path.join(DATA_DIR, 'index.json')) as f:
        index_data = json.load(f)
    context = dict(
        related_products=get_related_products(),
        page_title=index_data.get("page_title") or "Karma"
    )
    return render(request, 'mainapp/index.html', context=context)


def category(request):
    with open(os.path.join(DATA_DIR, 'category.json')) as f:
        category_data = json.load(f)
    context = dict(
        related_products=get_related_products(),
        page_title=category_data.get("page_title") or "Karma",
        categories=category_data.get("categories"),
        product_filters=category_data.get("product_filters"),
        products=category_data.get("products")
    )
    return render(request, 'mainapp/category.html', context=context)


def single_product(request):
    with open(os.path.join(DATA_DIR, 'single-product.json')) as f:
        single_product_data = json.load(f)
    context = dict(
        related_products=get_related_products(),
        page_title=single_product_data.get("page_title") or "Karma",
        product_description=single_product_data.get("product_description")
    )
    print(context)
    return render(request, 'mainapp/single-product.html', context=context)
