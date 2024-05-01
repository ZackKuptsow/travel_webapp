from decimal import Decimal
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
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
from simple_history.models import HistoricalRecords

from base.typed_dicts import BookingToDict

# NOT NECESSARY AT THE MOMENT -> switch foreign keys if re-implemented
# class UserProfile(Model):
#     """Model to store all basic user information."""

#     user = ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=CASCADE,
#     )

#     data_joined = DateTimeField(auto_now_add=True)

#     created_at = DateTimeField(auto_now_add=True)
#     updated_at = DateTimeField(auto_now_add=True)

#     history = HistoricalRecords()

#     class Meta:
#         db_table = "user_profiles"
#         get_latest_by = "created_at"
#         ordering = ("-created_at",)
#         verbose_name = "user_profile"
#         verbose_name_plural = "user_profiles"


class Address(Model):
    """Physical address model."""

    class Meta:
        db_table = "addresses"
        verbose_name = "address"
        verbose_name_plural = "addresses"

    full_name = CharField(max_length=512)
    address_line_1 = CharField(max_length=256)
    address_line_2 = CharField(max_length=256, blank=True, null=True)
    city_or_province = CharField(max_length=128)
    country = CharField(max_length=2)
    zipcode = CharField(max_length=16)

    location = PointField()

    @property
    def latitude(self) -> Decimal:
        """Get the latitude from the location point.

        Returns:
            Decimal: latitude
        """
        return Decimal(self.location.y)

    @property
    def longitude(self) -> Decimal:
        """Get the longitude from the location point.

        Returns:
            Decimal: longitude
        """
        return Decimal(self.location.x)


class Booking(Model):
    """Abstract model to track users involved and event information."""

    class Meta:
        abstract = True
        db_table = "bookings"
        get_latest_by = "created_at"
        ordering = ("-created_at",)
        verbose_name = "booking"
        verbose_name_plural = "bookings"

    admin = ForeignKey(User, on_delete=CASCADE, related_name="admin_bookings")
    invitees = ManyToManyField(
        User,
        related_name="invitee_bookings",
        blank=True,
    )

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

    history = HistoricalRecords(inherit=True)

    def to_dict(self) -> BookingToDict:
        """Convert model instance to dictionary.

        Returns:
            BookingToDict: dictionary representation of instance
        """
        return {
            "admin": self.admin.id,
            "invitees": list(self.invitees.all().values_list("id", flat=True)),
            "cost": self.cost,
            "name": self.name,
            "link": self.link,
            "start_date_time": self.start_date_time.isoformat(),
            "end_date_time": self.end_date_time.isoformat(),
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def _reassign_admin(self):
        """TODO: Handle re-assignment to invitees if admin is deleted or needs to be reassigned."""
        pass
