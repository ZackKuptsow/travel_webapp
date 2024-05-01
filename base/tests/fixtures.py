import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def auto_login_user(db, create_user: User) -> APIClient:
    """Authenticate a test user.

    Args:
        db: A pytest fixture for setting up and tearing down the database.
        create_user (User): A fixture function that creates and returns a new User instance.

    Returns:
        APIClient: An authenticated APIClient instance.
    """
    api_client = APIClient()
    api_client.force_authenticate(user=create_user)
    return api_client
