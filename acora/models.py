from django.db import models
from django.utils import timezone
class Partida(models.Model):
    codigo=models.charField(primary_key=True,max_length=20)
    estado=models.BooleanField(default=False)
    temporizador=models.TimeField(default=time.now)

class Equipo(models.Model):
    ide=models.CharField(primary_key=True,max_length=200)
    nombre=models.CharField(unique=True)
    puntaje=models.IntegerField(default=0)
    idPista=models.CharField()
    codigo=models.ForeignKey(Partida)

class Ranking(models.Model):
    idRanking=models.CharField()
    codigo=models.ForeignKey(Partida)
    
