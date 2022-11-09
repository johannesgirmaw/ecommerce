
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from ..product.models import Product

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer


@api_view(['POST'])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def checkout(request):
    print(request.data)
    serializer = OrderSerializer(data=request.data)
    items = []
    if serializer.is_valid():
        print("serializer-------------------", serializer)
        total_amount = sum(item.get(
            'quantity') * item.get('product').total_price for item in serializer.validated_data['items'])
        print(total_amount)
        if len(serializer.validated_data['items']) > 0:
            for item in serializer.validated_data['items']:
                price = item.get('price')
                product = item.get('product')
                quantity = item.get('quantity')
                print("item:", item)
                # product = Product.objects.get(pk=item.get('product'))
                item = {"price": price, "product": product,
                        "quantity": quantity}
                items.append(item)
        else:
            items = []
        # try:
        serializer.save(items=items,
                        user=request.user, total_amount=total_amount)
        print("serializer1:", serializer)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # except Exception:
        # return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
