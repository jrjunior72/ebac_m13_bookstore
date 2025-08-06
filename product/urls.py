from django.urls import include, path
from rest_framework import routers

from product.viewsets.product_viewset import ProductViewSet

router = routers.SimpleRouter()
router.register(r"product", ProductViewSet, basename="product")
#router.register(r"category", viewsets.CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]