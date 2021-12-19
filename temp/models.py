from django.db import models

# Create your models here.


class Dato(models.Model):
    id = models.BigIntegerField(primary_key=True)
    valor = models.IntegerField()
