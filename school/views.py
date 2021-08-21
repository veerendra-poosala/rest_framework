from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def home(request):
    return Response({'status':200,'message':'This is a Homepage'})
