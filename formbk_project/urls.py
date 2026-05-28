from rest_framework import routers
from .api import FormViewSet

router = routers.DefaultRouter()

router.register('forms', FormViewSet, 'form')

urlpatterns = router.urls