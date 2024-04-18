from rest_framework import serializers
from parking_slot.models import ParkingSlot
from parking_meter.models import ParkingMeter
from parking_meter.serializer import ParkingMeterSerializer

class ParkingSlotSerializer(serializers.ModelSerializer):
    parkingmeter = ParkingMeterSerializer()

    class Meta:
        model = ParkingSlot
        fields = ['slot_id', 'location', 'status', 'expiration', 'parkingmeter']