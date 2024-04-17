from decimal import Decimal, ROUND_HALF_UP
from django.contrib.auth.models import User
from django.db.models import (
    Avg,
    CASCADE,
    DateTimeField,
    DecimalField,
    ForeignKey,
    Model,
    TextField,
)
from simple_history.models import HistoricalRecords

from base.models import Booking


RATING_CHOICES = [
    (0.0, "0.0"),
    (0.5, "0.5"),
    (1.0, "1.0"),
    (1.5, "1.5"),
    (2.0, "2.0"),
    (2.5, "2.5"),
    (3.0, "3.0"),
    (3.5, "3.5"),
    (4.0, "4.0"),
    (4.5, "4.5"),
    (5.0, "5.0"),
]


class ActivityBooking(Booking):
    """Model representing a bookable activity."""

    class Meta:
        db_table = "bookings_activity"
        get_latest_by = "created_by"
        ordering = ("-created_at",)
        verbose_name = "activity"
        verbose_name_plural = "activities"

    @property
    def rating(self) -> Decimal:
        """Calculate the average rating based off all comments."""
        raw_average_rating = self.comments.aggregate(average_rating=Avg("rating"))[
            "average_rating"
        ]
        if raw_average_rating is not None:
            return (Decimal(raw_average_rating) * 2).quantize(
                Decimal("1"), rounding=ROUND_HALF_UP
            ) / 2
        return Decimal(0.0)


class ActivityComment(Model):
    """Model representing a user comment and review."""

    class Meta:
        db_table = "comments"
        get_latest_by = "created_at"
        ordering = ("-created_at",)
        verbose_name = "comment"
        verbose_name_plural = "comments"

    user = ForeignKey(User, on_delete=CASCADE, related_name="comments")
    activity_booking = ForeignKey(
        ActivityBooking, on_delete=CASCADE, related_name="comments"
    )
    comment = TextField(max_length=1024)
    rating = DecimalField(
        max_digits=2,
        decimal_places=1,
        choices=RATING_CHOICES,
        default=0,
        help_text="Rating on a scale of 0 to 5 in increments of 0.5",
    )

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)

    history = HistoricalRecords()
