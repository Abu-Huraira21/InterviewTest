from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()

router.register(r"events", EventViewSet, basename="events")


urlpatterns = [
    path("", include(router.urls)),
]

