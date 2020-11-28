from django.shortcuts import render, get_object_or_404
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
    category_products = Product.objects.filter(brand_name_id=category_pk)
    context = dict(
        brands=ProductBrand.objects.all(),
        products=category_products
    )
    return render(request, 'mainapp/category.html', context=context)


def product_page(request, product_pk=None):
    # context = dict(
    #     related_products=get_related_products(),
    #     page_title=single_product_data.get("page_title") or "Karma",
    #     product_description=single_product_data.get("product_description")
    # )
    product = get_object_or_404(Product, pk=product_pk)

    context = dict(
        product=product,
        related_products=get_related_products(),
    )

    return render(request, 'mainapp/product_page.html', context=context)
