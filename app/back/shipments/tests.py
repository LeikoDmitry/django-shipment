from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Shipment


class ShipmentsTests(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/v1/shipments/'
        self.shipment = Shipment.objects.create(title='Test', description='test', date_shipment=timezone.now())

    def test_list_shipment(self) -> None:
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 1)

    def test_detail_shipment(self) -> None:
        response = self.client.get(self.url + str(self.shipment.id) + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.shipment.title)

    def test_create_shipment(self) -> None:
        data = {
          'title': 'This is title',
          'description': 'This is description',
          'date_shipment': timezone.now()
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'This is title')

    def test_update_shipment(self) -> None:
        data = {
            'title': 'This is title',
            'description': 'This is description',
            'date_shipment': timezone.now()
        }
        response = self.client.put(self.url + str(self.shipment.id) + '/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'This is title')

    def test_delete_shipment(self) -> None:
        response = self.client.delete(self.url + str(self.shipment.id) + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
