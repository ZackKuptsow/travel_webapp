from decimal import Decimal
from typing import List, TypedDict


class BookingToDict(TypedDict):
    admin: int
    invitees: List[int]
    cost: Decimal | None
    name: str
    link: str | None
    start_date_time: str
    end_date_time: str
    status: str
    created_at: str
    updated_at: str
