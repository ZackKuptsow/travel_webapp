from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from factory import Faker, LazyAttribute, SubFactory, post_generation
from factory.django import DjangoModelFactory
from factory.random import random
from typing import List, Optional

from activity.models import ActivityBooking, ActivityComment, RATING_CHOICES
from base.tests.factories import AddressFactory, UserFactory


class ActivityBookingFactory(DjangoModelFactory):
    """Factory to generate ActivityBooking instances for testing."""

    class Meta:
        model = ActivityBooking

    admin = SubFactory(UserFactory)
    cost = Faker("pydecimal", left_digits=10, right_digits=2, positive=True)
    name = Faker("sentence", nb_words=4)
    link = Faker("url")
    start_date_time = LazyAttribute(lambda _: timezone.now())
    end_date_time = LazyAttribute(lambda obj: obj.start_date_time + timedelta(hours=2))
    status = Faker(
        "random_element",
        elements=[
            choice[0] for choice in ActivityBooking._meta.get_field("status").choices  # type: ignore [union-attr]
        ],
    )

    # TODO: limit faker phone number to 15 numbers
    # phone_number = Faker("phone_number")
    phone_number = "+12345678910"
    address = SubFactory(AddressFactory)

    created_at = LazyAttribute(lambda _: timezone.now())
    updated_at = LazyAttribute(lambda _: timezone.now())

    @post_generation
    def invitees(self, create: bool, extracted: Optional[List[User]], **kwargs):
        """Generate and/or set users to the invitees relationship.

        Args:
            create (bool): Whether the instance is being saved to the database
            extracted (Optional[List[User]]): Optional list of users that can be set as invitees
        """
        if create:
            invitees = (
                extracted
                if extracted
                else UserFactory.create_batch(random.randint(1, 10))
            )
            self.invitees.set(invitees)


class ActivityCommentFactory(DjangoModelFactory):
    """Factory to generate ActivityComment instances for testing."""

    class Meta:
        model = ActivityComment

    user = SubFactory(UserFactory)
    activity_booking = SubFactory(ActivityBookingFactory)
    rating = Faker("random_element", elements=[choice[0] for choice in RATING_CHOICES])
