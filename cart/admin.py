from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__email',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product_variant', 'quantity', 'created_at')
    search_fields = ('cart__user__email', 'product_variant__product__name')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
