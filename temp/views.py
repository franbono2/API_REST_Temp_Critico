from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from temp.utils import get_plot
from .models import Dato
from .serializers import DatoSerializer

# Create your views here.


class DatoList(generics.ListAPIView):
    queryset = Dato.objects.all()
    serializer_class = DatoSerializer


class DatoCreate(generics.CreateAPIView):
    queryset = Dato.objects.all()
    serializer_class = DatoSerializer

class DatoList10(generics.ListAPIView):
    queryset = Dato.objects.all()[:10]
    serializer_class = DatoSerializer

def main_view(request):
    qs = Dato.objects.all()[:10]
    x = [x.time for x in qs]
    y = [y.valor for y in qs]
    chart = get_plot(x, y)
    return render(request, 'main.html', {'chart' : chart})
