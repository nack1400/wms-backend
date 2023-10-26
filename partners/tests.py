from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer, Consignee
from .serializers import CustomerSerializer, ConsigneeSerializer


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


class ConsigneeAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse("consignee-list")
        self.valid_payload = {
            "name": "Consignee 1",
            "is_active": True,
            "memo": "Some memo for consignee",
        }

    def test_create_consignee(self):
        response = self.client.post(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Consignee.objects.count(), 1)
        self.assertEqual(Consignee.objects.get().name, "Consignee 1")

    def test_list_consignees(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Consignee.objects.count())

    def test_retrieve_consignee(self):
        consignee = Consignee.objects.create(name="Consignee 2")
        response = self.client.get(reverse("consignee-detail", args=[consignee.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], consignee.name)

    def test_update_consignee(self):
        consignee = Consignee.objects.create(name="Consignee 3")
        updated_data = {
            "name": "Updated Consignee",
            "is_active": False,
            "memo": "Updated memo",
        }
        response = self.client.put(
            reverse("consignee-detail", args=[consignee.id]),
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        consignee.refresh_from_db()
        self.assertEqual(consignee.name, "Updated Consignee")
        self.assertEqual(consignee.is_active, False)
        self.assertEqual(consignee.memo, "Updated memo")

    def test_delete_consignee(self):
        consignee = Consignee.objects.create(name="Consignee 4")
        response = self.client.delete(reverse("consignee-detail", args=[consignee.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Consignee.objects.count(), 0)
