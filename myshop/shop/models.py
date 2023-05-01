from django.db import models
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='Pending')
    promocode = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    receipt = models.ImageField(upload_to='receipts/', blank=True, null=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.buyer.username}'s order"
