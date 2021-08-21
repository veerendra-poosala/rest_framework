from django.db.models import fields
from rest_framework import serializers
from .models import *

class secuirity_staffSerializer(serializers.ModelSerializer):
    class Meta:
        model=secuirity_staffModel
        fields='__all__'