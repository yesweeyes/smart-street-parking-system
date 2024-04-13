from django.db import models
from parking_slot.models import ParkingSlot

class ParkingMeter(models.Model):
    class ParkingMeterStatusChoices(models.TextChoices):
        FUNCTIONAL = "FUNCTIONAL"
        NON_FUNCTIONAL = "NON_FUNCTIONAL"
        
    meter_id = models.AutoField(primary_key=True)
    slot = models.OneToOneField(ParkingSlot, on_delete=models.CASCADE)
    status = models.CharField(default=ParkingMeterStatusChoices.FUNCTIONAL, max_length=20, choices=ParkingMeterStatusChoices.choices)
    battery_level = models.IntegerField()