from django.urls import include, path
from rest_framework import routers
from .views import ShipmentViewSetList

router = routers.DefaultRouter()
router.register(r'shipments', ShipmentViewSetList)

urlpatterns = [
    path('', include(router.urls)),
]
