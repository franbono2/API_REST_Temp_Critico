from django.urls import path
from .views import DatoCreate, DatoList, DatoList10

urlpatterns = [
    path('nuevo/', DatoCreate.as_view()),
    path('listajson/', DatoList10.as_view()),
    path('', DatoList.as_view())
]
