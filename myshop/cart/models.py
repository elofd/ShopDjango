from django.db import models
from users.models import CustomUser
from shop.models import Product


class Cart(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.buyer.username}'s cart"
