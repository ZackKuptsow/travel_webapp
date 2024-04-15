import pytest

from base.tests.factories import UserFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestUserAuthAPI:
    def setup_method(self):
        self.client = APIClient()
        self.user_data = {
            "username": "test_user",
            "password": "test_password",
            "email": "test_user@example.com",
        }
        self.user = UserFactory(
            username="existing_user",
            email="existing_user@example.com",
            password="existing_password",
        )

    def test_create_user(self):
        response = self.client.post(reverse("base:user-list"), self.user_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["username"] == self.user_data["username"]

    def test_update_user(self):
        new_data = {
            "username": "updated_user",
            "password": "updated_password",
            "email": "updated_user@example.com",
        }
        response = self.client.put(
            reverse("base:user-detail", args=[self.user.id]), new_data
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == new_data["username"]

    def test_list_users(self):
        UserFactory.create_batch(3)
        response = self.client.get(reverse("base:user-list"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 4
