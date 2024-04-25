from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from parking_slot.models import ParkingSlot
from parking_slot.serializer import ParkingSlotSerializer

class ParkingSlotAPIView(APIView):
    def get(self, request):
        parking_slots = ParkingSlot.objects.all()
        serializer = ParkingSlotSerializer(parking_slots, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ParkingSlotSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        parking_slots = ParkingSlot.objects.all()
        parking_slots.delete()
        return Response(status=status.HTTP_200_OK)
    
class ParkingSlotDetailAPIView(APIView):
    def get(self, request, id):
        parking_slot = ParkingSlot.objects.get(slot_id=id)
        serializer = ParkingSlotSerializer(parking_slot, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, id):
        try:
            parking_slot = ParkingSlot.objects.get(id=id)
            serializer = ParkingSlotSerializer(parking_slot, data=request.data)  
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ParkingSlot.DoesNotExist:
            return Response({'error': 'Parking slot not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id):
        try:
            parking_slot = ParkingSlot.objects.get(id=id)
            parking_slot.delete()
            return Response(status=status.HTTP_200_OK)
        except ParkingSlot.DoesNotExist:
            return Response({'error': 'Parking meter not found'}, status=status.HTTP_404_NOT_FOUND)