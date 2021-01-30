from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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


class ShopUserProfile(models.Model):

    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(to=ShopUser, on_delete=models.CASCADE, unique=True, null=False, db_index=True)
    # ??? What is it below
    tagline = models.CharField(verbose_name='tags', max_length=128, blank=True)
    about_me = models.CharField(verbose_name='info about user', max_length=512, blank=True)
    gender = models.CharField(verbose_name='user gender', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
