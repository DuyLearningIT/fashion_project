from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'detail_address', 'phone')
    search_fields = ('user__email', 'district', 'phone')


admin.site.register(Address, AddressAdmin)
