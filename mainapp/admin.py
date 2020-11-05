from django.contrib import admin

from mainapp.models import ProductCategory, ProductBrand, Product

admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(Product)
