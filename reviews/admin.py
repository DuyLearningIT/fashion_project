from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'comment', 'created_at')
    search_fields = ('user__email', 'product__name', 'rating')


admin.site.register(Review, ReviewAdmin)
