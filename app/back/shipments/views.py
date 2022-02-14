from rest_framework import viewsets
from .models import Shipment
from .serializers import ShipmentSerializer


class ShipmentViewSetList(viewsets.ModelViewSet):
    queryset = Shipment.objects.order_by('-date_created')
    serializer_class = ShipmentSerializer
