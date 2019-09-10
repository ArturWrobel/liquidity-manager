from rest_framework.serializers import ModelSerializer
from .models import *

class CitiSerializer(ModelSerializer):
    class Meta:
        model = Citi
        fields = ["date", "inflows", "outflows"]