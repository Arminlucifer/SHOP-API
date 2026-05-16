from rest_framework import generics

from .mixins import UserQuerySetMixin
from . permissions import  IsStaffEditorPermission, IsOwnerOrReadOnly
from .models import Category, Product
from . serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateAPIView(
    UserQuerySetMixin,
    generics.ListCreateAPIView,
    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission has been set in settings
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(owner=self.request.user)


class ProductRetrieveUpdateDestroyAPIView(
    UserQuerySetMixin,
    generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'
    permission_classes = [
                            IsStaffEditorPermission |
                            IsOwnerOrReadOnly,
                          ]


