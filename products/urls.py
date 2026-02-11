from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ProductImageViewSet, ProductVariantViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('product-variants', ProductVariantViewSet)
router.register('product-images', ProductImageViewSet)

urlpatterns = router.urls
