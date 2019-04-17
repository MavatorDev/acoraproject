from django.db import models
from django.utils import timezone

class Partida(models.Model):
    codigo=models.CharField(primary_key=True,max_length=20,default='0')
    estado=models.BooleanField(default=False)
    temporizador=models.TimeField(default='50:00')

class Equipo(models.Model):
    cod=models.CharField(primary_key=True,max_length=20,default='0')
    nombre=models.CharField(unique=True,max_length=200)
    puntaje=models.IntegerField(default=0)
    idPista=models.CharField(max_length=20,default='0')
    codigo=models.ForeignKey(Partida,on_delete=models.CASCADE)

class Ranking(models.Model):
    idRanking=models.CharField(primary_key=True,max_length=200,default='0')
    codigo=models.ForeignKey(Partida,on_delete=models.CASCADE)
    
