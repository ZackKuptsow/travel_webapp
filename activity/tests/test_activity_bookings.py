import pytest
from decimal import Decimal, ROUND_HALF_UP
from factory import Iterator
from random import choice

from activity.models import RATING_CHOICES
from activity.tests.factories import ActivityBookingFactory, ActivityCommentFactory


@pytest.mark.django_db
class TestActivityBookings:
    """Test class for ActivityBooking."""

    def setup_method(self):
        """Create instances for tests below."""
        self.activity_booking = ActivityBookingFactory()

    def test_calculate_rating(self):
        """Test the ActivityBooking rating method.

        The method calls all ActvityComments related to an ActivityBooking.
        """
        size = 10
        ratings = [Decimal(choice(RATING_CHOICES)[1]) for _ in range(size)]
        ratings_iter = Iterator(ratings)
        ActivityCommentFactory.create_batch(
            size=size,
            activity_booking=self.activity_booking,
            rating=ratings_iter,
        )

        assert (
            self.activity_booking.rating
            == (Decimal(sum(ratings) / size) * 2).quantize(
                Decimal("1"), rounding=ROUND_HALF_UP
            )
            / 2
        )
