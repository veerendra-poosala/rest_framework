from django.db.models import fields
from rest_framework import serializers
from .models import *

class floor_inchargeSerializer(serializers.ModelSerializer):
    class Meta:
        model=floor_inchargeModel
        fields='__all__'