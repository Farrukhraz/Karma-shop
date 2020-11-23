from django.shortcuts import render
from mainapp.models import ProductCategory, ProductBrand, Product, DealsOfTheWeek, SingleFeature


def get_related_products() -> list:
    deals_of_the_week = DealsOfTheWeek.objects.all()
    related_products = list()
    for deal in deals_of_the_week:
        related_products.append(deal)
    return related_products


def index(request):
    single_features = SingleFeature.objects.all()
    context = dict(
        related_products=get_related_products(),
        single_features=single_features,
    )
    return render(request, 'mainapp/index.html', context=context)


def products(request, *args, **kwargs):
    shop_products = Product.objects.all()
    context = dict(
        brands=ProductBrand.objects.all(),
        products=shop_products
    )
    return render(request, 'mainapp/category.html', context=context)


def category_items(request, category_pk=None, *args, **kwargs):
    if category_pk is not None and category_pk in range(1, 4):
        category_products = [i for i in Product.objects.all() if i.brand_name_id == category_pk]
    else:
        # products = Product.objects.all()
        category_products = []
    context = dict(
        brands=ProductBrand.objects.all(),
        products=category_products
    )
    return render(request, 'mainapp/category.html', context=context)


def single_product(request):
    context = dict(
        related_products=get_related_products(),
        page_title=single_product_data.get("page_title") or "Karma",
        product_description=single_product_data.get("product_description")
    )
    return render(request, 'mainapp/single-product.html', context=context)
