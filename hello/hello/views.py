from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import ulSerializer
from .models import ul

class uploadView(CreateAPIView):
    queryset = ul.objects.all()
    serializer_class = ulSerializer