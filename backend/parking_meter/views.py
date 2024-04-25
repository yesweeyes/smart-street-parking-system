from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from parking_meter.models import ParkingMeter
from parking_meter.serializer import ParkingMeterSerializer

class ParkingMeterAPIView(APIView):
    def get(self, request):
        parking_meters = ParkingMeter.objects.all()
        serializer = ParkingMeterSerializer(parking_meters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def post(self, request):
        serializer = ParkingMeterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        parking_meters = ParkingMeter.objects.all()
        if parking_meters:
            parking_meters.delete()
        return Response(status=status.HTTP_200_OK)
    
class ParkingMeterDetailAPIView(APIView):
    def get(self, request, id):
        parking_meter = ParkingMeter.objects.get(id=id)
        serializer = ParkingMeterSerializer(parking_meter)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    def patch(self, request, id):
        try:
            parking_meter = ParkingMeter.objects.get(id=id)
            serializer = ParkingMeterSerializer(parking_meter, data=request.data)  
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ParkingMeter.DoesNotExist:
            return Response({'error': 'Parking meter not found'}, status=status.HTTP_404_NOT_FOUND)
    
                
    def delete(self, request, id):
        try:
            parking_meter = ParkingMeter.objects.get(id=id)
            parking_meter.delete()
            return Response(status=status.HTTP_200_OK)
        except ParkingMeter.DoesNotExist:
            return Response({'error': 'Parking meter not found'}, status=status.HTTP_404_NOT_FOUND)
