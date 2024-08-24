from network.apps import NetworkConfig
from rest_framework.routers import DefaultRouter

from network.views import NetworkEntityViewSet

app_name = NetworkConfig.name

router = DefaultRouter()
router.register('', NetworkEntityViewSet, basename='network')

urlpatterns = router.urls
