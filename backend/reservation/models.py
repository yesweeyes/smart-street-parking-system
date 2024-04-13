from django.db import models
from parking_slot.models import ParkingSlot

class Reservation(models.Model):
    
    class ReservationStatusChoices(models.TextChoices):
        ACTIVE = "ACTIVE"
        CANCELLED = "CANCELLED"
    
    reservation_id = models.AutoField(primary_key=True)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(default=ReservationStatusChoices.ACTIVE, max_length=20, choices=ReservationStatusChoices.choices)
