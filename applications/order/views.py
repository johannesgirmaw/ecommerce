
from applications.category.models import Category
from rest_framework import generics
from django.http import Http404

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer, MyOrderSerializer
from rest_framework.permissions import IsAuthenticated

# Do the validation for the product qauntity if it is finished
# and update the quantity of the product


class OrderCheckout(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer = OrderSerializer(data=self.request.data)
        items = []
        if serializer.is_valid():

            total_amount = sum(item.get(
                'quantity') * item.get('product').total_price for item in serializer.validated_data['items'])

            if len(serializer.validated_data['items']) > 0:
                print(serializer.validated_data)
                for item in serializer.validated_data['items']:
                    product = item.get('product')
                    quantity = item.get('quantity')
                    item = {"product": product,
                            "quantity": quantity}
                    items.append(item)
            else:
                items = []
            serializer.save(items=items,
                            user=self.request.user, total_amount=total_amount)


class OrdersList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    # def get(self, pk, format=None):
    #     orders = Order.objects.filter(pk=pk, user=self.request.user)
    #     serializer = MyOrderSerializer(orders, many=True)
    #     return Response(serializer.data)

    def perform_update(self, request, serializer):
        print(self, request, serializer)
