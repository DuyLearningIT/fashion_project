from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'total_amount', 'created_at')
    search_fields = ('user__email', 'status')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_variant', 'quantity', 'price', 'product')
    search_fields = ('order__id', 'product_variant__product__name')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
