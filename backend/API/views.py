from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from . permissions import  IsStaffEditorPermission, IsOwnerOrReadOnly

from .models import Category, Product
from . serializers import CategorySerializer, ProductSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateAPIView(
    generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission has been set in settings

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [
                          IsStaffEditorPermission |
                          IsOwnerOrReadOnly,
                          ]


