from django.shortcuts import render
from rest_framework import authentication
from rest_framework import permissions
from .models import secuirity_staffModel
from .serializers import *
from rest_framework import status,viewsets
from rest_framework.response import Response
#from rest_framework.authentication import BaseAuthentication, BasicAuthentication
#from rest_framework.permissions import BasePermission, IsAdminUser
# Create views using Model view set

class secuirity_staffViewset(viewsets.ModelViewSet):
    queryset=secuirity_staffModel.objects.all()
    serializer_class=secuirity_staffSerializer

    