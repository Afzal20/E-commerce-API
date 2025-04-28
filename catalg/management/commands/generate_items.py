import os
import random
import uuid  # For unique product_id generation
from django.core.management.base import BaseCommand
from catalg.models import Item, Category, ItemType, Rating, Color, ItemImage, ItemSize, Size, ItemColor

# Define the image directory
IMAGE_DIR = r"./media/Products"

def get_all_images():
    """Retrieve all .jpg images from the given directory."""
    return [f for f in os.listdir(IMAGE_DIR) if f.endswith('.jpg')]

class Command(BaseCommand):
    help = 'Generate sample items with images, sizes, and colors'

    def handle(self, *args, **kwargs):
        self.create_items()

    def create_items(self):
        categories = Category.objects.all()
        item_types = ItemType.objects.all()
        ratings = Rating.objects.all()
        colors = Color.objects.all()
        sizes = Size.objects.all()
        images = get_all_images()

        if not images:
            self.stdout.write(self.style.ERROR("No .jpg images found in the directory."))
            return

        for i in range(50):
            product_id = f'prod-{uuid.uuid4().hex[:12]}'
            
            item = Item.objects.create(
                title=f'Item {i + 1}',
                image=f'Products/{random.choice(images)}',  # Adjusting the path
                ratings=random.choice(ratings) if ratings else None,
                price=random.randint(10, 500),
                number_of_items=random.randint(1, 100),
                discount_price=random.randint(5, 400),
                product_id=product_id,
                brand_name=f'Brand {random.choice(["A", "B", "C"])}',
                category=random.choice(categories) if categories else None,
                type=random.choice(item_types) if item_types else None,
                description=f'Description for item {i + 1}',
                is_featured=random.choice([True, False]),
                is_bestselling=random.choice([True, False]),
            )
            
            # Add extra images
            for _ in range(random.randint(1, 5)):
                ItemImage.objects.create(
                    item=item,
                    image=f'Products/{random.choice(images)}'
                )

            # Add sizes
            for size in random.sample(list(sizes), min(3, len(sizes))):
                ItemSize.objects.create(
                    item=item,
                    size=size,
                    price_for_this_size=random.randint(10, 500)
                )

            # Add colors
            for color in random.sample(list(colors), min(3, len(colors))):
                ItemColor.objects.create(
                    item=item,
                    color=color
                )

            self.stdout.write(self.style.SUCCESS(f'Created {item.title} with product_id {item.product_id}'))
