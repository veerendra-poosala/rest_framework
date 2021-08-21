from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import *

class principalSerializers(serializers.ModelSerializer):
    class Meta:
        model=principalModel
        fields='__all__'