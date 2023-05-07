from django.contrib import admin

from .models import Product, Order, Category, OrderItem


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'price', 'discount', 'stock', 'category', 'author')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline]
    list_display = ('pk', 'buyer', 'delivery_address', 'promocode', 'status', 'get_total_cost', 'paid')
    def get_total_cost(self, object):
        return object.get_total_cost()
    get_total_cost.short_description = 'Total cost'


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'description')


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

