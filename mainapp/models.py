from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="name", max_length=64, unique=True)
    description = models.TextField(verbose_name="description", blank=True)

    def __str__(self):
        return self.name


class ProductBrand(models.Model):
    name = models.CharField(verbose_name="name", max_length=64, unique=True)
    description = models.TextField(verbose_name="description", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='product name', max_length=64)
    brand_name = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='product short description', max_length=60, blank=True)
    description = models.TextField(verbose_name='product description', blank=True)
    price = models.DecimalField(verbose_name='product price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='quantity in stock', default=0)

    def __str__(self):
        return f"{self.name} - Category:({self.category.name}); Brand: ({self.brand_name})"
