from django.core.management.base import BaseCommand
from catalg.models import Color

class Command(BaseCommand):
    help = 'Populates the Color model with initial data'

    def handle(self, *args, **kwargs):
        colors = [
            {"name": "Red", "code": "#FF0000"},
            {"name": "Green", "code": "#00FF00"},
            {"name": "Blue", "code": "#0000FF"},
            {"name": "Yellow", "code": "#FFFF00"},
            {"name": "Black", "code": "#000000"},
            {"name": "White", "code": "#FFFFFF"},
            # Add more colors as needed
        ]

        for color_data in colors:
            Color.objects.get_or_create(name=color_data['name'], code=color_data['code'])

        self.stdout.write(self.style.SUCCESS('Successfully populated colors!'))
