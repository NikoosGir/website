from rest_framework import routers
from .views import BrandViewSet, BodyViewSet, TransmissionViewSet, DriveTypeViewSet, CarViewSet, CommentViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('brands', BrandViewSet)
router.register('bodys', BodyViewSet)
router.register('transmissions', TransmissionViewSet)
router.register('drive_types', DriveTypeViewSet)
router.register('car_models', CarViewSet)
router.register('comments', CommentViewSet)
router.register('posts', PostViewSet)
urlpatterns = router.urls