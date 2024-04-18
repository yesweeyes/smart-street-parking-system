from rest_framework import serializers
from parking_meter.models import ParkingMeter

class ParkingMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingMeter
        fields = ['meter_id', 'status', 'battery_level']