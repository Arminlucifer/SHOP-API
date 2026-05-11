from django.urls import path

from . views import ProductRetrieveUpdateDestroyAPIView, ProductListCreateAPIView


urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]