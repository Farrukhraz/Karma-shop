from django.db import models


class AuthPageImages(models.Model):

    name = models.CharField(verbose_name='image name', max_length=64, blank=True)
    image = models.ImageField(upload_to="auth_page_images", blank=True)

    def __str__(self):
        return f"Auth page image name: {self.name}, path: {self.image.url}"
