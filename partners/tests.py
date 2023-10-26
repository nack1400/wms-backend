from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer, Consignee, Carrier, DeliveryAddress, Bank, Contact


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


class CarrierTests(APITestCase):
    def setUp(self):
        self.carrier_data = {
            "name": "Test Carrier",
            "is_active": True,
            "memo": "Test Memo",
        }
        self.url = reverse("carrier-list")

    def test_create_carrier(self):
        response = self.client.post(self.url, self.carrier_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Carrier.objects.count(), 1)
        self.assertEqual(Carrier.objects.get().name, "Test Carrier")

    def test_list_carriers(self):
        Carrier.objects.create(**self.carrier_data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_carrier(self):
        carrier = Carrier.objects.create(**self.carrier_data)
        url = reverse("carrier-detail", args=[carrier.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Carrier")

    def test_update_carrier(self):
        carrier = Carrier.objects.create(**self.carrier_data)
        url = reverse("carrier-detail", args=[carrier.pk])
        updated_data = {"name": "Updated Carrier", "memo": "Updated Memo"}
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Carrier")
        self.assertEqual(response.data["memo"], "Updated Memo")

    def test_delete_carrier(self):
        carrier = Carrier.objects.create(**self.carrier_data)
        url = reverse("carrier-detail", args=[carrier.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Carrier.objects.count(), 0)


class DeliveryAddressTests(APITestCase):
    def setUp(self):
        self.url = reverse("delivery-address-list")
        self.valid_payload = {
            "name": "Delivery Address 1",
            "address": "123 Main St",
            "is_active": True,
            "memo": "Some memo for delivery address",
        }

    def test_create_delivery_address(self):
        response = self.client.post(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DeliveryAddress.objects.count(), 1)
        self.assertEqual(DeliveryAddress.objects.get().name, "Delivery Address 1")

    def test_list_delivery_addresses(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), DeliveryAddress.objects.count())

    def test_retrieve_delivery_address(self):
        delivery_address = DeliveryAddress.objects.create(name="Delivery Address 2")
        response = self.client.get(
            reverse("delivery-address-detail", args=[delivery_address.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], delivery_address.name)

    def test_update_delivery_address(self):
        delivery_address = DeliveryAddress.objects.create(name="Delivery Address 3")
        updated_data = {
            "name": "Updated Delivery Address",
            "is_active": False,
            "memo": "Updated memo for delivery address",
        }
        response = self.client.put(
            reverse("delivery-address-detail", args=[delivery_address.id]),
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        delivery_address.refresh_from_db()
        self.assertEqual(delivery_address.name, "Updated Delivery Address")
        self.assertEqual(delivery_address.is_active, False)
        self.assertEqual(delivery_address.memo, "Updated memo for delivery address")

    def test_delete_delivery_address(self):
        delivery_address = DeliveryAddress.objects.create(name="Delivery Address 4")
        response = self.client.delete(
            reverse("delivery-address-detail", args=[delivery_address.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DeliveryAddress.objects.count(), 0)


class BankTests(APITestCase):
    def setUp(self):
        self.bank_data = {
            "name": "Test Bank",
            "account_number": "1234567890",
            "account_type": "Savings",
            "memo": "Test Memo",
        }
        self.bank = Bank.objects.create(**self.bank_data)
        self.bank_url = reverse("bank-list")

    def test_create_bank(self):
        response = self.client.post(self.bank_url, self.bank_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bank.objects.count(), 2)

    def test_create_bank_with_customer(self):
        customer_data = {
            "name": "Test Customer",
            "is_active": True,
            "memo": "Customer Memo",
        }
        customer = Customer.objects.create(**customer_data)
        bank_data = {
            "name": "Test Bank",
            "account_number": "1234567890",
            "account_type": "Savings",
            "memo": "Test Memo",
            "customer": customer.pk,
        }
        response = self.client.post(self.bank_url, bank_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bank.objects.count(), 2)
        self.assertEqual(response.data["customer"], customer.pk)

    def test_list_banks(self):
        response = self.client.get(self.bank_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_bank(self):
        url = reverse("bank-detail", args=[self.bank.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Bank")

    def test_update_bank(self):
        updated_data = {
            "name": "Updated Bank",
            "account_number": "9876543210",
            "account_type": "Checking",
            "memo": "Updated Memo",
        }
        url = reverse("bank-detail", args=[self.bank.pk])
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Bank")
        self.assertEqual(response.data["account_number"], "9876543210")

    def test_delete_bank(self):
        url = reverse("bank-detail", args=[self.bank.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bank.objects.count(), 0)


class ContactTests(APITestCase):
    def setUp(self):
        self.contact_data = {
            "name": "Test Contact",
            "email": "test@example.com",
            "phone": "123-456-7890",
            "address": "Test Address",
            "memo": "Test Memo",
        }
        self.contact = Contact.objects.create(**self.contact_data)
        self.contact_url = reverse("contact-list")

    def test_create_contact(self):
        response = self.client.post(self.contact_url, self.contact_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 2)

    def test_create_contact_with_customer(self):
        customer_data = {
            "name": "Test Customer",
            "is_active": True,
            "memo": "Customer Memo",
        }
        customer = Customer.objects.create(**customer_data)
        contact_data = {
            "name": "Test Contact",
            "email": "test@example.com",
            "phone": "123-456-7890",
            "address": "Test Address",
            "memo": "Test Memo",
            "customer": customer.pk,
        }
        response = self.client.post(self.contact_url, contact_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 2)
        self.assertEqual(response.data["customer"], customer.pk)

    def test_list_contacts(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_contact(self):
        url = reverse("contact-detail", args=[self.contact.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Contact")

    def test_update_contact(self):
        updated_data = {
            "name": "Updated Contact",
            "email": "updated@example.com",
            "phone": "987-654-3210",
            "address": "Updated Address",
            "memo": "Updated Memo",
        }
        url = reverse("contact-detail", args=[self.contact.pk])
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Contact")
        self.assertEqual(response.data["email"], "updated@example.com")

    def test_delete_contact(self):
        url = reverse("contact-detail", args=[self.contact.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contact.objects.count(), 0)
