from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from categories.models import Category
from .models import Product


class ProductTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category", key="test", sequence_number=1
        )
        self.product_data = {
            "name": "Test Product",
            "packer": "Test Packer",
            "brand": "Test Brand",
            "identification_code": "12345",
            "memo": "Test Memo",
            "category": self.category,
        }
        self.product = Product.objects.create(**self.product_data)
        self.url_list = reverse("product-list")
        self.url_detail = reverse("product-detail", args=[self.product.id])

    def test_get_product_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        original_sequence_number = self.category.sequence_number
        new_category_data = {
            "name": "New Test Category",
            "key": "new_test",
            "sequence_number": 2,
        }
        new_category = Category.objects.create(**new_category_data)

        new_product_data = {
            "name": "New Test Product",
            "packer": "New Test Packer",
            "brand": "New Test Brand",
            "identification_code": "12345",
            "memo": "New Test Memo",
            "category": new_category.pk,
        }

        response = self.client.post(self.url_list, new_product_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        new_category.refresh_from_db()
        self.assertEqual(new_category.sequence_number, original_sequence_number + 1)

    def test_get_product_detail(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        updated_data = {
            "name": "Updated Product",
            "packer": "Updated Packer",
            "brand": "Updated Brand",
        }
        response = self.client.put(self.url_detail, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, updated_data["name"])
        self.assertEqual(self.product.packer, updated_data["packer"])

    def test_delete_product(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
