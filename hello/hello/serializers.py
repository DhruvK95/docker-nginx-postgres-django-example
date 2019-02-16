from rest_framework import serializers
from .models import ul

class ulSerializer(serializers.ModelSerializer):
    class Meta:
        model = ul
        fields = ['myFile',]
