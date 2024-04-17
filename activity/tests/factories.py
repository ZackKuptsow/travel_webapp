from django.utils import timezone
from factory import Faker, LazyAttribute, SubFactory
from factory.django import DjangoModelFactory

from activity.models import ActivityBooking, ActivityComment, RATING_CHOICES
from base.tests.factories import UserFactory


class ActivityBookingFactory(DjangoModelFactory):
    class Meta:
        model = ActivityBooking

    admin = SubFactory(UserFactory)
    cost = Faker("pydecimal", left_digits=10, right_digits=2, positive=True)
    name = Faker("sentence", nb_words=4)
    link = Faker("url")
    start_date_time = LazyAttribute(lambda _: timezone.now())
    end_date_time = LazyAttribute(
        lambda obj: obj.start_date_time + timezone.timedelta(hours=2)
    )
    status = Faker(
        "random_element",
        elements=[
            choice[0] for choice in ActivityBooking._meta.get_field("status").choices
        ],
    )
    created_at = LazyAttribute(lambda _: timezone.now())
    updated_at = LazyAttribute(lambda _: timezone.now())


class ActivityCommentFactory(DjangoModelFactory):
    class Meta:
        model = ActivityComment

    user = SubFactory(UserFactory)
    activity_booking = SubFactory(ActivityBookingFactory)
    rating = Faker("random_element", elements=[choice[0] for choice in RATING_CHOICES])
