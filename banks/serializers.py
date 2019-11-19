from rest_framework import serializers
from .models import *

class CitiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citi
        fields = ["date", "inflows", "outflows"]