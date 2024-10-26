import random
import uuid  # For unique product_id generation
from django.core.management.base import BaseCommand
from catalg.models import Item, Category, ItemType, Rating, Color, ItemImage, ItemSize, Size, ItemColor

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
        images = [
            'logo-2-300x124.png', 'products02.jpg', 'products03.jpg', 
            'products04.jpg', 'products05.jpg', 'products07.jpg', 
            'products08.jpg', 'products09.jpg', 'products10.jpg', 
            'products11.jpg', 'products12.jpg', 'products13.jpg', 
            'products14.jpg', 'products15.jpg', 'products16.jpg', 
            'products17.jpg', 'products18.jpg', 'products19.jpg', 
            'products20.jpg', 'products21.jpg', 'products22.jpg', 
            'products23.jpg', 'products24.jpg', 'products25.jpg', 
            'products26.jpg', 'products27.jpg', 'transparent-2-qr-1024x1024.png'
        ]

        for i in range(100):
            # Generate a unique product ID
            product_id = f'prod-{uuid.uuid4()}'
            
            # Create the item
            item = Item.objects.create(
                title=f'Item {i + 1}',
                image=f'images/{random.choice(images)}',  # Adjust the path if necessary
                ratings=random.choice(ratings),
                price=random.randint(10, 500),
                number_of_items=random.randint(1, 100),  # Ensure this is set
                discount_price=random.randint(5, 400),
                product_id=product_id,  # Use UUID to ensure uniqueness
                brand_name=f'Brand {random.choice(["A", "B", "C"])}',
                category=random.choice(categories) if categories else None,
                type=random.choice(item_types) if item_types else None,
                description=f'Description for item {i + 1}',
                is_featured=random.choice([True, False]),
                is_bestselling=random.choice([True, False]),
            )
            
            # Add extra images for the item
            for _ in range(random.randint(1, 5)):  # Randomly add between 1 and 5 images
                ItemImage.objects.create(
                    item=item,
                    image=f'item_images/{random.choice(images)}'  # Use the same pool of images
                )

            # Add sizes for the item
            for size in random.sample(list(sizes), random.randint(1, min(3, len(sizes)))):  # Randomly add 1 to 3 sizes
                ItemSize.objects.create(
                    item=item,
                    size=size,
                    price_for_this_size=random.randint(10, 500)  # Random price for each size
                )

            # Add colors for the item
            for color in random.sample(list(colors), random.randint(1, min(3, len(colors)))):  # Randomly add 1 to 3 colors
                ItemColor.objects.create(
                    item=item,
                    color=color
                )

            print(f'Created {item.title} with product_id {item.product_id}, {item.images.count()} images, '
                  f'{item.item_size.count()} sizes, and {item.item_color.count()} colors')
