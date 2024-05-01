from rest_framework.viewsets import ModelViewSet

from activity.models import ActivityBooking, ActivityComment
from activity.serializers import ActivityBookingSerializer, ActivityCommentSerializer
from activity.respositories import ActivityBookingRepository


class ActivityBookingViewSet(ModelViewSet):
    """Viewset for ActivityBooking."""

    queryset = ActivityBooking.objects.all()
    serializer_class = ActivityBookingSerializer

    def perform_create(self, serializer: ActivityBookingSerializer):
        """Create valid ActivityBooking.

        Args:
            serializer (ActivityBookingSerializer): serializer to validate data
        """
        ActivityBookingRepository.create_booking(**serializer.validated_data)

    def perform_update(self, serializer: ActivityBookingSerializer):
        """Update valid ActivityBooking.

        Args:
            serializer (ActivityBookingSerializer): serializer to validate data
        """
        ActivityBookingRepository.update_booking(
            self.get_object().id, **serializer.validated_data
        )


class ActivityCommentViewSet(ModelViewSet):
    """Viewset for ActivityComment."""

    queryset = ActivityComment.objects.all()
    serializer_class = ActivityCommentSerializer
