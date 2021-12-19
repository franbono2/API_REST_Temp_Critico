from django.db import models

# Create your models here.


class Dato(models.Model):
    time = models.BigIntegerField(primary_key=True)
    valor = models.IntegerField()
