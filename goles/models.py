from datetime import timezone
from django.db import models

# Create your models here.

class Goles(models.Model):

    fecha = models.DateField('%Y-%m-%d', default=timezone.now)
    hora = models.TimeField()
    equipo = models.CharField(max_length=30)
    rival = models.CharField(max_length=30)
    minuto = models.IntegerField()
    parcial = models.CharField(max_length=30)


