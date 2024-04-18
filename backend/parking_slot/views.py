from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from parking_slot.models import ParkingSlot
from parking_slot.serializer import ParkingSlotSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

class ParkingSlotAPIView(APIView):
    def get(self, request):
        parking_slots_with_meter = ParkingSlot.objects.select_related("parkingmeter")
        serializer = ParkingSlotSerializer(parking_slots_with_meter, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ParkingSlotDetailAPIView(APIView):
    def delete(self, request, id):
        parking_slot = ParkingSlot.objects.get(slot_id=id)
        parking_slot.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
