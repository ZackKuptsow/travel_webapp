from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    ManyToManyField,
    Model,
    URLField,
)
from django.conf import settings
from simple_history.models import HistoricalRecords


class UserProfile(Model):
    """Model to store all basic user information."""

    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
    )

    data_joined = DateTimeField(auto_now_add=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    class Meta:
        db_table = "user_profiles"
        get_latest_by = "created_at"
        ordering = ("-created_at",)
        verbose_name = "user_profile"
        verbose_name_plural = "user_profiles"


class Booking(Model):
    """Abstract model to track users involved and event information."""

    admin = ForeignKey(UserProfile, on_delete=CASCADE, related_name="admin_bookings")
    invitees = ManyToManyField(UserProfile, related_name="invitee_bookings")

    cost = DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    name = CharField(max_length=1000)
    link = URLField(max_length=1000, blank=True, null=True)

    start_date_time = DateTimeField()
    end_date_time = DateTimeField()
    status = CharField(
        max_length=100,
        choices=(
            ("canceled", "Canceled"),
            ("completed", "Completed"),
            ("confirmed", "Confirmed"),
            ("pending", "Pending"),
        ),
    )

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    class Meta:
        abstract = True
        db_table = "bookings"
        get_latest_by = "created_at"
        ordering = ("-created_at",)
        verbose_name = "booking"
        verbose_name_plural = "bookings"

    def _reassign_admin(self):
        """TODO: Handle reassignment to invitees if admin is deleted or needs to be reassigned."""
        pass
