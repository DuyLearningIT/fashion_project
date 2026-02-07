from django.contrib import admin
from .models import PaymentTransaction


class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'status',
                    'transaction_code', 'paid_at')
    search_fields = ('user__email', 'order__id', 'transaction_code')


admin.site.register(PaymentTransaction, PaymentTransactionAdmin)
