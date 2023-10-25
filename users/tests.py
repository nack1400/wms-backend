from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User


class UserTests(APITestCase):
    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "password": "kwon1234",
            "email": "test@example.com",
            "phone": "123-456-7890",
            "role": "employee",
        }
        self.user = User.objects.create_user(**self.user_data)
        self.url = reverse("user-list")

    def test_create_user(self):
        new_user_data = {
            "username": "newuser1",
            "password": "kwon1234",
            "email": "newuser@example.com",
            "phone": "987-654-3210",
            "role": "manager",
        }
        response = self.client.post(self.url, new_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_create_user_no_username(self):
        new_user_data = {
            "password": "kwon1234",
            "email": "newuser@example.com",
            "phone": "987-654-3210",
            "role": "manager",
        }
        response = self.client.post(self.url, new_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_no_password(self):
        new_user_data = {
            "username": "newuser1",
            "email": "newuser@example.com",
            "phone": "987-654-3210",
            "role": "manager",
        }
        response = self.client.post(self.url, new_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), User.objects.count())

    def test_get_user_detail(self):
        detail_url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)

    def test_update_user(self):
        detail_url = reverse("user-detail", args=[self.user.id])
        updated_data = {
            "username": "newusername",
            "email": "newemail@example.com",
        }
        response = self.client.put(detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        detail_url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
