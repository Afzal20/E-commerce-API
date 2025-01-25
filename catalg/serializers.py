from rest_framework import serializers
from .models import (
    Districts, Category, ItemType, Size, Rating, Color,
    Item, ItemImage, ItemSize, ItemColor, Cart, Order, OrderItems,
    Slider, BillingAddress, Payment, Coupon, Refund
)

class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = ['id', 'title']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ['id', 'name']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'value']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'code']

class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['id', 'image']

class ItemSizeSerializer(serializers.ModelSerializer):
    size = SizeSerializer()
    
    class Meta:
        model = ItemSize
        fields = ['id', 'size', 'price_for_this_size']

class ItemColorSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    
    class Meta:
        model = ItemColor
        fields = ['id', 'color']

# Main Item Serializer

class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True)  # Get all related images
    item_size = ItemSizeSerializer(many=True)  # Get all related sizes with details
    item_color = ItemColorSerializer(many=True)  # Get all related colors with details
    category = CategorySerializer()  # Nested serializer for category
    type = ItemTypeSerializer()  # Nested serializer for item type
    ratings = RatingSerializer()  # Nested serializer for ratings

    class Meta:
        model = Item
        fields = [
            'id', 'title', 'image', 'ratings', 'price', 'number_of_items',
            'discount_price', 'product_id', 'brand_name', 'category', 'type',
            'description', 'is_featured', 'is_bestselling', 'images', 'item_size', 'item_color'
        ]



# Order and Cart related Serializers

class OrderItemsSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    
    class Meta:
        model = OrderItems
        fields = ['id', 'item', 'item_size', 'item_color_code', 'quantity', 'order_status']

class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ['id', 'user', 'street_address', 'apartment_address', 'country', 'zip']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'timestamp', 'payment_method', 'charge_id', 'success']

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'amount']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemsSerializer(many=True)
    billing_address = BillingAddressSerializer()
    payment = PaymentSerializer()
    coupon = CouponSerializer()
    
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'order_items', 'ordered', 'start_date', 'ordered_date',
            'district', 'Address', 'Apartment', 'billing_address', 'payment',
            'coupon', 'being_delivered', 'received', 'refund_requested', 'refund_granted'
        ]

class CartSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    applied_coupon = CouponSerializer()
    
    class Meta:
        model = Cart
        fields = '__all__'
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'image', 'title']

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = ['id', 'order', 'reason', 'accepted', 'email']

# Admin-related Serializers

class AdminBillingAddressSerializer(BillingAddressSerializer):
    class Meta(BillingAddressSerializer.Meta):
        fields = BillingAddressSerializer.Meta.fields

class AdminPaymentSerializer(PaymentSerializer):
    class Meta(PaymentSerializer.Meta):
        fields = PaymentSerializer.Meta.fields

class AdminCouponSerializer(CouponSerializer):
    class Meta(CouponSerializer.Meta):
        fields = CouponSerializer.Meta.fields
