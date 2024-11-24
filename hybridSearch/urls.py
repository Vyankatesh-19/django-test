from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import MagazineInfoViewSet,MagazineContentViewSet

router = SimpleRouter()
router.register('magazineinfo', MagazineInfoViewSet, basename='magazineinfo')
router.register('magazinecontent', MagazineContentViewSet, basename='magazinecontent')

urlpatterns = router.urls