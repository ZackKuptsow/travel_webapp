from django.urls import include, path
from rest_framework.routers import DefaultRouter

from activity.views import ActivityBookingViewSet, ActivityCommentViewSet

router = DefaultRouter()

router.register(r"bookings", ActivityBookingViewSet)
router.register(r"comments", ActivityCommentViewSet)

urlpatterns = [path("", include(router.urls))]
