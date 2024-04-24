from django.urls import path
from django.urls import include

urlpatterns = [
    path("meter/", include("parking_meter.urls"), name="parking-meter"),
]