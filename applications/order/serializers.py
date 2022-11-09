from rest_framework import serializers

from .models import Order, OrderItem

from applications.product.serializers import ProductSerializer


class MyOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )


class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "place",
            "phone",
            "items",
            "order_status",
            "total_amount"
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "place",
            "phone",
            "items",
            "order_status",
            "total_amount"
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        print("items_data:-----", items_data)
        print("validated_data:------", validated_data)

        order = Order.objects.create(**validated_data)
        print("order:", order)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
