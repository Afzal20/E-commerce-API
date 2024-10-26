from django.core.management.base import BaseCommand
from catalg.models import ItemType

class Command(BaseCommand):
    help = 'Populates the ItemType model with popular Bangladeshi fashion item types'

    def handle(self, *args, **kwargs):
        item_types = [
            'Casual',
            'Formal',
            'Party Wear',
            'Traditional',
            'Ethnic',
            'Sportswear',
            'Fusion',
            'Winter Wear',
            'Summer Wear',
            'Office Wear'
        ]

        for item_type_name in item_types:
            item_type, created = ItemType.objects.get_or_create(name=item_type_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created item type: {item_type_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Item type {item_type_name} already exists'))
