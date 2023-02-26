from rest_framework import routers
from .api import GolesViewSet

router = routers.DefaultRouter()
router.register('api/goles', GolesViewSet, 'goles')

urlpatterns = router.urls