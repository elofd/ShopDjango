from django.contrib import admin

from .models import Product, Order, Category


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('pk', 'buyer', 'delivery_address', 'promocode', 'status', )


admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
admin.site.register(Category)

