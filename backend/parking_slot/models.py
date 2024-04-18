from django.db import models

class ParkingSlot(models.Model):
    
    class ParkingSlotStatusChoices(models.TextChoices):
        OCCUPIED = "OCCUPIED"
        VACANT = "VACANT"
        
    slot_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    status = models.CharField(default=ParkingSlotStatusChoices.VACANT ,max_length=10, choices=ParkingSlotStatusChoices.choices)
    expiration = models.DateTimeField(blank=True, null=True)
    
    def clean(self):
        if self.status == self.ParkingSlotStatusChoices.OCCUPIED and not self.expiration:
            raise Exception("Expiration must be provided for a vacant parking slot")
        
    def __str__(self):
        return self.location