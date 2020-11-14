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


class HotOffers(models.Model):
    title = models.CharField(verbose_name='product title', max_length=64)
    description = models.TextField(verbose_name='product description', max_length=200, blank=True)
    image = models.ImageField(upload_to='hot_offers_images', blank=True)

    def __str__(self):
        return f"Hot offer product name: {self.title}"


class DealsOfTheWeek(models.Model):
    name = models.CharField(verbose_name="product name", max_length=64)
    price = models.DecimalField(verbose_name="product name", max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(verbose_name="product image", blank=True)

    def __str__(self):
        return f"Deals of the week - Name: {self.name}; Price: {self.price}"


