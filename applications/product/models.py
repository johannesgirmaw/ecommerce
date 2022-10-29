from django.db import models
from applications.category.models import Category
from django.utils.html import mark_safe
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    category_id = models.ForeignKey(
        Category, related_name="products",  on_delete=models.CASCADE)
    total_price = models.FloatField()
    actual_price = models.FloatField()
    delivery_price = models.FloatField()
    quantity = models.IntegerField()
    product_image = models.ImageField(
        upload_to="product/", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.product_name
