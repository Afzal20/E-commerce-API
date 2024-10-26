from django.core.management.base import BaseCommand
from catalg.models import Size

class Command(BaseCommand):
    help = 'Populates the Size model with common T-shirt sizes'

    def handle(self, *args, **kwargs):
        sizes = [
            "XS", "S", "M", "L", "XL", "XXL", "XXXL"
        ]

        for size_name in sizes:
            Size.objects.get_or_create(name=size_name)

        self.stdout.write(self.style.SUCCESS('Successfully populated sizes!'))
