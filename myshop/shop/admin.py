from django.contrib import admin

from .models import Product, Order, Category


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'price', 'discount', 'stock', 'category', 'author')


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('pk', 'buyer', 'delivery_address', 'promocode', 'status', )


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'description')


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

