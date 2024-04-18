from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from parking_slot.models import ParkingSlot
from parking_slot.serializer import ParkingSlotSerializer
from parking_slot.serializer import LimitedParkingSlotSerializer
from rest_framework import status

class ParkingSlotAPIView(APIView):
    def get(self, request):
        parking_slots_with_meter = ParkingSlot.objects.select_related("parkingmeter")
        serializer = ParkingSlotSerializer(parking_slots_with_meter, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = LimitedParkingSlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ParkingSlotDetailAPIView(APIView):
    def delete(self, request, id):
        parking_slot = ParkingSlot.objects.get(slot_id=id)
        parking_slot.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
