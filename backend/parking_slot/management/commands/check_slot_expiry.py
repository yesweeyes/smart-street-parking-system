# management/commands/events.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from parking_slot.models import ParkingSlot

class Command(BaseCommand):
    help = 'Check parking slots for expiration and update their status'

    def handle(self, *args, **options):
        current_time = timezone.now()
        expired_slots = ParkingSlot.objects.filter(status=ParkingSlot.ParkingSlotStatusChoices.OCCUPIED, expiration__lte=current_time)
        for slot in expired_slots:
            slot.status = ParkingSlot.ParkingSlotStatusChoices.VACANT
            slot.expiration = None
            slot.save()
