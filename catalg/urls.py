from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AddToCartView, CartListView, DistrictsViewSet, CategoryViewSet, ItemTypeViewSet, RemoveFromCartView,
    SizeViewSet, RatingViewSet, ColorViewSet, ItemViewSet, ItemImageViewSet,
    ItemSizeViewSet, ItemColorViewSet, OrderItemsViewSet, 
    OrderViewSet, SliderViewSet, BillingAddressViewSet, PaymentViewSet,
    CouponViewSet, RefundViewSet, get_item_by_product_id
)

router = DefaultRouter()
router.register(r'districts', DistrictsViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'item-types', ItemTypeViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'items', ItemViewSet)
router.register(r'item-images', ItemImageViewSet)
router.register(r'item-sizes', ItemSizeViewSet)
router.register(r'item-colors', ItemColorViewSet)
# router.register(r'carts', CartViewSet)
router.register(r'order-items', OrderItemsViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'sliders', SliderViewSet)
router.register(r'billing-addresses', BillingAddressViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'refunds', RefundViewSet)

# Custom route for fetching a single product by product_id
urlpatterns = [
    path('', include(router.urls)),
    path('items/<str:product_id>/', get_item_by_product_id, name='item-by-product-id'),
]

urlpatterns += [
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]