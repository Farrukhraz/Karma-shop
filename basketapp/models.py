from django.contrib.auth import get_user_model
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(verbose_name="время", auto_now_add=True)

    @property
    def product_cost(self):
        """Get current product cost"""
        return self.product.price * self.quantity
