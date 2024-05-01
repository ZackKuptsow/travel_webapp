from decimal import Decimal

from base.typed_dicts import BookingToDict


class ActivityBookingToDict(BookingToDict):
    phone_number: str
    address: int | None
    rating: Decimal
