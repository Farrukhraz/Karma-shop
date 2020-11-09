import os
import json
from django.shortcuts import render
from karma.settings import BASE_DIR
from mainapp.models import ProductCategory, ProductBrand, Product

DATA_DIR = os.path.join(BASE_DIR, 'data', 'mainapp')

with open(os.path.join(DATA_DIR, 'index.json')) as f:
    index_data = json.load(f)
with open(os.path.join(DATA_DIR, 'related_products.json'), encoding='utf-8') as f:
    related_products_data = json.load(f)
with open(os.path.join(DATA_DIR, 'category.json'), encoding='utf-8') as f:
    category_data = json.load(f)
with open(os.path.join(DATA_DIR, 'single-product.json'), encoding='utf-8') as f:
    single_product_data = json.load(f)


def get_related_products() -> dict:
    related_products = related_products_data.get("related_products") or dict()
    return related_products


def index(request):
    context = dict(
        related_products=get_related_products(),
        page_title=index_data.get("page_title") or "Karma",
        single_features=index_data.get("single_features"),
        products=index_data.get("products")
    )
    return render(request, 'mainapp/index.html', context=context)


def category(request, pk=None, *args, **kwargs):
    if pk is not None and pk in range(1, 4):
        products = [i for i in Product.objects.all() if i.brand_name_id == pk]
    else:
        products = Product.objects.all()
    context = dict(
        brands=ProductBrand.objects.all(),
        products=products
    )
    return render(request, 'mainapp/category.html', context=context)


# def category(request):
#     context = dict(
#         related_products=get_related_products(),
#         page_title=category_data.get("page_title") or "Karma",
#         categories=category_data.get("categories"),
#         product_filters=category_data.get("product_filters"),
#         products=category_data.get("products")
#     )
#     return render(request, 'mainapp/category.html', context=context)


def single_product(request):
    context = dict(
        related_products=get_related_products(),
        page_title=single_product_data.get("page_title") or "Karma",
        product_description=single_product_data.get("product_description")
    )
    return render(request, 'mainapp/single-product.html', context=context)
