from rest_framework.routers import DefaultRouter

from .viewsets import ProductView

router = DefaultRouter()

router.register('product-abc', ProductView, basename='product-abc')

urlpatterns = router.urls