from django.contrib.auth.models import User
from django.db import models

from applications.product.models import Product
from commons.authentication.models import CustomUser


class order_status(models.IntegerChoices):
    CREATED = 100
    REJECTED = 101
    PENDING = 102
    DELIVERED = 103


class Order(models.Model):
    user = models.ForeignKey(
        CustomUser, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(
        max_digits=1000, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2, null=True)
    # quantity = models.IntegerField(default=1)

    order_status = models.IntegerField(
        choices=order_status.choices, default=order_status.CREATED)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.CASCADE)
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '__all__'
