from django.shortcuts import render
from .models import Phone
from .serializers import CarSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView



# class CarListApiView(generics.ListAPIView):
#     queryset = Phone.objects.all()
#     serializer_class = CarSerializer
#

class PhoneListApiView(APIView):
    def get(self, request):
        cars = Phone.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

class PhoneCreateApiView(generics.CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = CarSerializer

class PhoneEditApiView(generics.UpdateAPIView):
    queryset = Phone.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'

class PhoneDeleteApiView(generics.DestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = CarSerializer


class PhoneDetailApiView(generics.RetrieveAPIView):
    queryset = Phone.objects.all()
    serializer_class = CarSerializer




