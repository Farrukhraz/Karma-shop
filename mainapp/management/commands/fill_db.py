from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Fill data in db'

    def handle(self, *args, **options):
        print("Hello from fill_db script")