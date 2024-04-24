from rest_framework import serializers
from parking_slot.models import ParkingSlot
from parking_slot.serializer import ParkingSlotSerializer
from parking_meter.models import ParkingMeter

class ParkingMeterSerializer(serializers.ModelSerializer):
    slot = ParkingSlotSerializer(required=False)  

    class Meta:
        model = ParkingMeter
        fields = '__all__'

    def create(self, validated_data):
        slot_data = validated_data.pop('slot', None) 

        if slot_data:
            slot = ParkingSlot.objects.create(**slot_data)  
            validated_data['slot'] = slot  

        return ParkingMeter.objects.create(**validated_data) 