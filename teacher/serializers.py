from rest_framework import serializers
from .models import *

#creating serializer class
class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=teacherModel
        fields='__all__'