from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Category


class CategoryTests(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(
            name="Category 1", key="cat1", billing_unit="Unit 1"
        )
        self.category2 = Category.objects.create(
            name="Category 2", key="cat2", billing_unit="Unit 2"
        )
        self.url_list = reverse("category-list")
        self.url_detail1 = reverse("category-detail", args=[self.category1.id])
        self.url_detail2 = reverse("category-detail", args=[self.category2.id])

    def test_get_category_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_category(self):
        data = {
            "name": "Category 3",
            "billing_unit": "Unit 3",
            "key": "cat3",
            "parent": None,
        }
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 3)
        created_category = Category.objects.get(name="Category 3")
        self.assertEqual(created_category.key, "cat3")

    def test_create_child_categories(self):
        data1 = {
            "name": "Child Category 1",
            "billing_unit": "Unit 1",
            "parent": self.category1.id,
            "key": "child_cat1",
        }
        response1 = self.client.post(self.url_list, data1, format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 3)
        child_category1 = Category.objects.get(name="Child Category 1")
        self.assertEqual(child_category1.level, self.category1.level + 1)

        data2 = {
            "name": "Child Category 2",
            "billing_unit": "Unit 2",
            "parent": self.category1.id,
            "key": "child_cat2",
        }
        response2 = self.client.post(self.url_list, data2, format="json")
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 4)
        child_category2 = Category.objects.get(name="Child Category 2")
        self.assertEqual(child_category2.level, self.category1.level + 1)

    def test_create_category_without_key(self):
        data = {
            "name": "Category Without Key",
            "billing_unit": "Unit",
            "parent": None,
        }
        response = self.client.post(self.url_list, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 2)

    def test_create_duplicate_key_category(self):
        data1 = {
            "name": "Duplicate Category",
            "billing_unit": "Unit",
            "key": "duplicate_cat",
            "parent": None,
        }
        response1 = self.client.post(self.url_list, data1, format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 3)

        data2 = {
            "name": "Another Duplicate Category",
            "billing_unit": "Unit",
            "key": "duplicate_cat",
            "parent": None,
        }
        response2 = self.client.post(self.url_list, data2, format="json")
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 3)

    def test_get_category_detail(self):
        response = self.client.get(self.url_detail1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Category 1")

    def test_get_nonexistent_category_detail(self):
        nonexistent_id = 9999
        response = self.client.get(reverse("category-detail", args=[nonexistent_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_category(self):
        data = {"name": "Updated Category", "billing_unit": "Updated Unit"}
        response = self.client.put(self.url_detail1, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Category.objects.get(pk=self.category1.id).name, "Updated Category"
        )

    def test_delete_category(self):
        response = self.client.delete(self.url_detail1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 1)
