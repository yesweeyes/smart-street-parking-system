from django.db import models

class ParkingSlot(models.Model):
    
    class ParkingSlotStatusChoices(models.TextChoices):
        OCCUPIED = "Occupied"
        VACANT = "Vacant"
        
    slot_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    status = models.CharField(default=ParkingSlotStatusChoices.VACANT ,max_length=10, choices=ParkingSlotStatusChoices.choices)
    expiration = models.DateTimeField()