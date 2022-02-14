from django.db import models


class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    date_shipment = models.DateTimeField('date_shipment')
    date_created = models.DateTimeField('date created', auto_now=True)

    def __str__(self):
        return self.title

