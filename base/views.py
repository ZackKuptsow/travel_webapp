from base.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """Create, retrieve/list and update actions for the User model."""

    lookup_field = "id"
    queryset = User.objects.all()
    serializer_class = UserSerializer
