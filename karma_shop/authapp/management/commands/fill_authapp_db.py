from django.core.management.base import BaseCommand
from authapp.models import AuthPageImages

import json
import os

JSON_PATH = 'authapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        page_images = load_from_json('page_images')
        AuthPageImages.objects.all().delete()
        for page_image in page_images:
            page_image = page_image.get('fields')
            new_page_image = AuthPageImages(**page_image)
            new_page_image.save()
