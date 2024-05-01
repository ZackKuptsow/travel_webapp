from django.db.models import QuerySet
from typing import Tuple

from activity.models import ActivityBooking, ActivityComment


class ActivityBookingRepository:
    """Repository for ActivityBookings."""

    @staticmethod
    def create_booking(**kwargs) -> ActivityBooking:
        """Create booking from data passed in.

        Returns:
            ActivityBooking: created booking
        """
        invitees = kwargs.pop("invitees", None)
        activity_booking = ActivityBooking.objects.create(**kwargs)
        if invitees:
            activity_booking.invitees.set(invitees)

        return activity_booking

    @staticmethod
    def get_booking_by_id(booking_id: int) -> ActivityBooking:
        """Get booking by its booking id.

        Args:
            booking_id (int): booking id

        Returns:
            ActivityBooking: retrieved booking
        """
        return ActivityBooking.objects.get(id=booking_id)

    @staticmethod
    def update_booking(booking_id: int, **kwargs) -> Tuple[bool, str]:
        """Update booking by id and updated data passed in.

        Args:
            booking_id (int): booking id

        Returns:
            Tuple[bool, Optional[str]]: success, error
        """
        try:
            ActivityBooking.objects.filter(id=booking_id).update(**kwargs)
            return True, ""
        except ActivityBooking.DoesNotExist as error:
            return False, str(error)


class ActivityCommentRepository:
    """Repository for ActivityComments."""

    @staticmethod
    def get_comments_by_booking_id(booking_id: int) -> QuerySet[ActivityComment]:
        """Retrieve all comments associated with a booking."""
        return ActivityComment.objects.filter(activity_booking_id=booking_id)
