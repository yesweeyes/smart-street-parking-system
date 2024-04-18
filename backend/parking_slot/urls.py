from django.urls import path
from parking_slot.views import ParkingSlotAPIView

urlpatterns = [
    path("all/", ParkingSlotAPIView.as_view(), name="parking-slots-all"),
]