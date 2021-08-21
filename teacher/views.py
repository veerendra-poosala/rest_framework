from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin
# Creating views by using Generic API View Mixins 

class readTeacherDetails(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=teacherModel.objects.all()
    serializer_class=teacherSerializer
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class updateTeacherDetails(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=teacherModel.objects.all()
    serializer_class=teacherSerializer
    def get(self,request,**kwargs):
       return self.retrieve(request,**kwargs)
    def post(self,request,**kwargs):
    
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.delete(request,**kwargs)