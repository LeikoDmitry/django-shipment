from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Shipment


class ShipmentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shipment
        fields = ['id', 'title', 'description', 'date_shipment', 'date_created']
