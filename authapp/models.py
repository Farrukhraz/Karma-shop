from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class AuthPageImages(models.Model):

    name = models.CharField(verbose_name='image name', max_length=64, blank=True)
    image = models.ImageField(upload_to="auth_page_images", blank=True)

    def __str__(self):
        return f"Auth page image name: {self.name}, path: {self.image.url}"


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", blank=True)
    age = models.PositiveIntegerField(verbose_name="возраст", default=18)

    activation_key = models.CharField(verbose_name="activation key", max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=now() + timedelta(hours=24))

    is_verified = models.BooleanField(verbose_name="is user verified", default=False)

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True
