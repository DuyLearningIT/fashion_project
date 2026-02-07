from django.contrib import admin
from .models import Category, Product, ProductVariant, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',
                    'base_price', 'status', 'created_at')
    search_fields = ('name', 'category__name',)


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'color', 'stock_quantity', 'price')
    search_fields = ('product__name',)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_url')
    search_fields = ('product__name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
