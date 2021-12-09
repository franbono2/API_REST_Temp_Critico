from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dato
from .serializers import DatoSerializer

# Create your views here.
class DatoList(generics.ListAPIView):
    queryset = Dato.objects.all()
    serializer_class = DatoSerializer

class DatoCreate(generics.CreateAPIView):
    queryset = Dato.objects.all()
    serializer_class = DatoSerializer
