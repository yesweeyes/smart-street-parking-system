from django.urls import path
from backend.parking_meter.views import ParkingMeterAPIView
from backend.parking_meter.views import ParkingMeterDetailAPIView

urlpatterns = [
    path("", ParkingMeterAPIView.as_view(), name="parking-meter-all"),
    path("<int: id>/", ParkingMeterDetailAPIView.as_view(), "parking-meter-detail"),
]
