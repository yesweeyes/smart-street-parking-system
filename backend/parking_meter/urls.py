from django.urls import path
from backend.parking_meter.views import ParkingMeterAPIView

urlpatterns = [
    path("", ParkingMeterAPIView.as_view(), name="parking-meter-all"),
]
