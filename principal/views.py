from django.shortcuts import render
from rest_framework.response import Response
from .models import principalModel
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView,UpdateAPIView




# here i want create models by using CONCRETE GENERIC VIEWS

class createPrincipalDetils(CreateAPIView):
    queryset=principalModel.objects.all()
    serializer_class=principalSerializers

class listPrincipalDetails(ListAPIView):
    queryset=principalModel.objects.all()
    serializer_class=principalSerializers

class RUDPrincipalDetails(RetrieveUpdateDestroyAPIView):
    queryset=principalModel.objects.all()
    serializer_class=principalSerializers