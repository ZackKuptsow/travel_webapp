import pytest
from rest_framework import status
from rest_framework.test import APIClient

from activity.tests.factories import ActivityBookingFactory


@pytest.mark.django_db
class TestActivityBookingAPI:
    """Test the APIs related to ActivityBookings."""

    client = APIClient()

    def test_create_activity_booking(self):
        """Test the POST creation of an ActivityBooking."""
        activity_booking = ActivityBookingFactory()
        url = "/api/activity/bookings/"

        response = self.client.post(url, activity_booking.to_dict(), format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert "phone_number" in response.data
