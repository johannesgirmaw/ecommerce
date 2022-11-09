from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email',
                    'address', 'place', 'phone', 'order_status', 'created_at',)


admin.site.register(Order, OrderAdmin)
