from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)