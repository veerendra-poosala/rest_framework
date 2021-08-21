from django.db.models import fields
from rest_framework import serializers
from .models import *


#creating studentSerializer for studentModel to convert the data into json format
#and here i am using ModelSerializer

class studentSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=studentModel
        fields='__all__'