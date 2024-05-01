from rest_framework.serializers import ModelSerializer

from activity.models import ActivityBooking, ActivityComment


class ActivityBookingSerializer(ModelSerializer):
    """Handles serialization/deserialization of ActivityBooking model instances."""

    class Meta:
        model = ActivityBooking
        fields = "__all__"


class ActivityCommentSerializer(ModelSerializer):
    """Handles serialization/deserialization of ActivityComment model instances."""

    class Meta:
        model = ActivityComment
        fields = "__all__"
