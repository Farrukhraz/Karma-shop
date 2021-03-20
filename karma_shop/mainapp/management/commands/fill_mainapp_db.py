from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, ProductBrand, HotOffers, DealsOfTheWeek

import json
import os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            category = category.get('fields')
            new_category = ProductCategory(**category)
            new_category.save()

        brands = load_from_json('brands')
        ProductBrand.objects.all().delete()
        for brand in brands:
            brand = brand.get('fields')
            new_brand = ProductBrand(**brand)
            new_brand.save()

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            product = product.get('fields')
            category_name = product["category"]
            brand_name = product["brand_name"]
            # Получаем категорию и бренд по имени
            _category = ProductCategory.objects.get(name=category_name)
            _brand = ProductBrand.objects.get(name=brand_name)
            # Заменяем название категории и бренда объектом
            product['category'] = _category
            product['brand_name'] = _brand
            new_product = Product(**product)
            new_product.save()

        hot_offers = load_from_json('hot_offers')
        HotOffers.objects.all().delete()
        for hot_offer in hot_offers:
            hot_offer = hot_offer.get('fields')
            new_hot_offer = HotOffers(**hot_offer)
            new_hot_offer.save()

        deals_of_the_weeks = load_from_json('deals_of_the_week')
        DealsOfTheWeek.objects.all().delete()
        for deal_of_the_week in deals_of_the_weeks:
            deal_of_the_week = deal_of_the_week.get('fields')
            new_deal_of_the_week = DealsOfTheWeek(**deal_of_the_week)
            new_deal_of_the_week.save()

        if not ShopUser.objects.filter(username='django').exists():
            ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
