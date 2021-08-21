from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response


# creating functions for CRUD Operations
#creating read function

@api_view(['GET'])
def readStudentDetails(request):
    #creating query set for studentModel
    q_set=studentModel.objects.all()
    #creating serializer
    serializer=studentSerializer(q_set,many=True)
    return Response(serializer.data)


#Creating create function

@api_view(['POST'])
def createStudentDetails(request):
    q_set=studentModel.objects.all()

    serializer=studentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateStudentDetails(request,id):

    q_set=studentModel.objects.get(id=id)

    serializer=studentSerializer(instance=q_set,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteStudentDetails(request,id):
    q_set=studentModel.objects.get(id=id)

  
    q_set.delete()
    
    return Response('Deleted successfully')