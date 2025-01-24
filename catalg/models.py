from django.conf import settings
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class Districts(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ItemType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rating(models.Model):
    value = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.value} Stars"

class Color(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    ratings = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    number_of_items = models.IntegerField()
    discount_price = models.IntegerField()
    product_id = models.CharField(max_length=20, unique=True)
    brand_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=260)
    is_featured = models.BooleanField(default=False)
    is_bestselling = models.BooleanField(default=False)
    colors = models.ManyToManyField(Color, through='ItemColor')

    def __str__(self):
        return self.title

    def get_add_to_url(self):
        return reverse('add_to_cart', kwargs={'product_id': self.product_id})

    def remove_from_cart_url(self):
        return reverse('remove_from_cart', kwargs={'product_id': self.product_id})

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return f"Image for {self.item.title}"

class ItemSize(models.Model):
    item = models.ForeignKey(Item, related_name='item_size', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price_for_this_size = models.IntegerField()

    def __str__(self):
        return self.size.name

class ItemColor(models.Model):
    item = models.ForeignKey(Item, related_name='item_color', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.color.name
    
class Slider(models.Model):
    image = models.ImageField(upload_to='images/slider')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)
    charge_id = models.CharField(max_length=50)
    success = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment: {self.charge_id} - {self.amount}"

class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True)
    amount = models.FloatField()

    def __str__(self):
        return self.code

class Refund(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"Refund for Order: {self.order}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField('Item', through='OrderItems')
    ordered = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    ordered_date = models.DateField(blank=True, null=True)
    district = models.ForeignKey('Districts', on_delete=models.SET_NULL, null=True)
    Address = models.CharField(max_length=300, null=True)
    Apartment = models.CharField(max_length=300, null=True)
    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    item_size = models.CharField(max_length=10)
    item_color_code = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.title} (Order: {self.order.id})"


class Cart(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    item_color_code = models.CharField(max_length=100)
    item_size = models.CharField(max_length=10)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    order_status = models.BooleanField(default=False)
    applied_coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('user_name', 'item', 'ordered', 'item_size', 'item_color_code')

    def __str__(self):
        return f"{self.quantity} of {self.product_Id}"
