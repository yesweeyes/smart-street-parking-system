from django.urls import path
from parking_meter.views import ParkingMeterAPIView
from parking_meter.views import ParkingMeterDetailAPIView
from parking_meter.views import ParkingMeterAllAPIView

urlpatterns = [
    path("", ParkingMeterAPIView.as_view(), name="parking-meter"),
    path("get-all/", ParkingMeterAllAPIView.as_view(), name="parking-meter-all"),
    path("<int:id>/", ParkingMeterDetailAPIView.as_view(), name="parking-meter-detail"),
]
