from django.contrib import admin

from mainapp.models import ProductCategory, ProductBrand, Product, HotOffers, DealsOfTheWeek

admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(HotOffers)
admin.site.register(DealsOfTheWeek)
