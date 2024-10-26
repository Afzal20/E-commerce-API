from django.core.management.base import BaseCommand
from catalg.models import Rating

class Command(BaseCommand):
    help = 'Populates the Rating model with initial data'

    def handle(self, *args, **kwargs):
        ratings = [
            1, 2, 3, 4, 5
        ]

        for value in ratings:
            Rating.objects.get_or_create(value=value)

        self.stdout.write(self.style.SUCCESS('Successfully populated ratings!'))
