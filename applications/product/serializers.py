from unicodedata import category
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            "id",
            "category_id",
            "product_name",
            "description",
            "total_price",
            "actual_price",
            "delivery_price",
            "quantity",
            "product_image",
        )

        model = Product
