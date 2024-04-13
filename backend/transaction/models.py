from django.db import models
from parking_slot.models import ParkingSlot

class Transaction(models.Model):
    
    class TransactionPaymentStatusChoices(models.TextChoices):
        PAID = "PAID"
        UNPAID = "UNPAID"
    
    transaction_id = models.AutoField(primary_key=True)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(default=TransactionPaymentStatusChoices.UNPAID, max_length=20, choices=TransactionPaymentStatusChoices.choices)