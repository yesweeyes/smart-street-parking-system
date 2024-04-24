from django.urls import path
from parking_slot.views import ParkingSlotAPIView
from parking_slot.views import ParkingSlotDetailAPIView

urlpatterns = [
    path("", ParkingSlotAPIView.as_view(), name="parking-slot-all"),
    path("<int:id>/", ParkingSlotDetailAPIView.as_view(), name="parking-slot-detail"),
]