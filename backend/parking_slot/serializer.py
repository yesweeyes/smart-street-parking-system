from rest_framework import serializers
from parking_slot.models import ParkingSlot
class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = '__all__'