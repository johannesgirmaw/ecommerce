from urllib import response
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

import django_filters.rest_framework
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'description',
                     'total_price', 'id']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
