from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer
from .serializers import CustomerSerializer


class CustomerTests(APITestCase):
    def setUp(self):
        self.customer_data = {
            "name": "Customer 1",
            "is_active": True,
            "memo": "This is a test customer",
        }
        self.customer = Customer.objects.create(**self.customer_data)
        self.url = reverse("customer-list")

    def test_create_customer(self):
        new_customer_data = {
            "name": "New Customer",
            "is_active": True,
            "memo": "This is a new customer",
        }
        response = self.client.post(self.url, new_customer_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)

    def test_create_customer_invalid_data(self):
        invalid_customer_data = {
            "is_active": True,
            "memo": "This is an invalid customer",
        }
        response = self.client.post(self.url, invalid_customer_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_customers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Customer.objects.count())

    def test_get_customer_detail(self):
        detail_url = reverse("customer-detail", args=[self.customer.id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.customer.name)

    def test_update_customer(self):
        detail_url = reverse("customer-detail", args=[self.customer.id])
        updated_data = {
            "name": "Updated Customer",
            "memo": "This is an updated customer",
        }
        response = self.client.put(detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, "Updated Customer")
        self.assertEqual(self.customer.memo, "This is an updated customer")

    def test_delete_customer(self):
        detail_url = reverse("customer-detail", args=[self.customer.id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
