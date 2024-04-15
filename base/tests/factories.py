import factory

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda name: f"user{name}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")

    @factory.post_generation
    def mbox(obj, create, extracted, *args, **kwargs):
        if not create:
            return

        obj.set_password("default_password")
