from django.contrib import admin
from .models import Shipment


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date_created')
    list_filter = ('title', 'date_shipment')

