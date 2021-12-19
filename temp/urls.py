from django.urls import path
from .views import DatoCreate, DatoList

urlpatterns = [
    path('nuevo/', DatoCreate.as_view()),
    path('', DatoList.as_view()),
]
