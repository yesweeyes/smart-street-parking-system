from django.urls import path
from parking_slot.views import ParkingSlotAPIView, ParkingSlotDetailAPIView

urlpatterns = [
    path("all/", ParkingSlotAPIView.as_view(), name="parking-slots-all"),
    path("<int:id>/", ParkingSlotDetailAPIView.as_view(), name="parking-slot-detail")
]