from django.contrib.auth.models import User
from django.db.models import QuerySet
from factory import (
    Faker,
    LazyAttribute,
    LazyFunction,
    Sequence,
    post_generation,
)
from factory.django import DjangoModelFactory

from base.models import Address
from base.tests.utils import generate_geo_point, generate_three_letter_country_code


class AddressFactory(DjangoModelFactory):
    """Factory to generate Address instances for testing."""

    class Meta:
        model = Address

    full_name = Faker("name")
    address_line_1 = Faker("street_address")
    address_line_2 = "Apt 123"
    city_or_province = Faker("city")
    country = LazyFunction(generate_three_letter_country_code)
    zipcode = Faker("zipcode")

    location = LazyFunction(generate_geo_point)


class UserFactory(DjangoModelFactory):
    """Factory to generate User instances for testing."""

    class Meta:
        model = User

    username = Sequence(lambda name: f"user{name}")
    email = LazyAttribute(lambda obj: f"{obj.username}@example.com")

    @post_generation
    def mbox(obj: User, create: bool, extracted: QuerySet[User], *args, **kwargs):
        """Post generation hook to set user password.

        Args:
            obj (User): user generated without password
            create (bool): on create boolean
            extracted (QuerySet[User]): users passed into factory
        """
        if not create:
            return

        obj.set_password("default_password")
