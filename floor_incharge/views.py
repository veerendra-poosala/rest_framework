
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class floor_incharegeViewset(viewsets.ViewSet):
    def list(self,request):
        querySet=floor_inchargeModel.objects.all()
        serializer=floor_inchargeSerializer(querySet,many=True)
        return Response(serializer.data)
    def create(self,request):
        querySet=floor_inchargeModel.objects.all()
        serializer=floor_inchargeSerializer(querySet,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk):
        pk=id
        if id is not None:
            querySet=floor_inchargeModel.objects.get(id=id)
            serializer=floor_inchargeSerializer(querySet)
            return Response(serializer.data)
        
    def update(self,request,pk):
        id=pk
        querySet=floor_inchargeModel.objects.get(pk=id)
        serializer=floor_inchargeSerializer(querySet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'updation completed'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        id=pk
        querySet=floor_inchargeModel.objects.get(pk=id)
        request.delete()
        return Response({'msg':'deleted successfully'})