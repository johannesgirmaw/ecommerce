from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework import filters
from rest_framework import status, authentication, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name', 'id']
    permission_classes = [IsAuthenticated]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name', 'id']
    permission_classes = [IsAuthenticated]
