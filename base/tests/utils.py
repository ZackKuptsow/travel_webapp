from django.contrib.gis.geos import Point
from factory.faker import faker

callable_faker = faker.Faker()


def generate_geo_point() -> Point:
    """Generate a Point for PointField usage.

    Returns:
        Point: geo point of latitude and longitude
    """
    return Point(
        float(callable_faker.longitude()),
        float(callable_faker.latitude()),
    )


def generate_three_letter_country_code() -> str:
    """Generate alpha-3 country code.

    Example:
        United States -> USA
        Costa Rica -> CRI

    Returns:
        str: three letter country code
    """
    return callable_faker.country_code()
