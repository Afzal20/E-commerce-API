from django.core.management.base import BaseCommand
from catalg.models import Category

class Command(BaseCommand):
    help = 'Populates the Category model with popular Bangladeshi fashion categories'

    def handle(self, *args, **kwargs):
        categories = [
            'Sarees',
            'Kurtis',
            'Salwar Kameez',
            'Lehenga',
            'Shirts',
            'Panjabi',
            'T-Shirts',
            'Pants',
            'Hijabs',
            'Traditional Jewelry'
        ]

        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created category: {category_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Category {category_name} already exists'))