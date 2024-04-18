from django.urls import path
from django.urls import include

urlpatterns = [
    path("slot/", include("parking_slot.urls"), name="parking-slot"),
    path("meter/", include("parking_meter.urls"), name="parking-meter"),
]