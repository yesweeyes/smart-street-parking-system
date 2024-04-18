from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from parking_slot.models import ParkingSlot
from parking_slot.serializer import ParkingSlotSerializer

class ParkingSlotAPIView(APIView):
    def get(self, request):
        parking_slots_with_meter = ParkingSlot.objects.select_related("parkingmeter")
        serializer = ParkingSlotSerializer(parking_slots_with_meter, many=True)
        return Response(serializer.data)
