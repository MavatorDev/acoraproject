from django.db import models
from django.utils import timezone

class Partida(models.Model):
    codigo=models.CharField(primary_key=True,max_length=20,default='0')
    estado=models.BooleanField(default=False)
    temporizador=models.TimeField(default='00:00')

def getCod():
   return Partida.objects.get(codigo=1);

class Equipo(models.Model):
    cod=models.CharField(primary_key=True,max_length=20,default='o0',blank=True)
    nombre=models.CharField(max_length=200,default='sinNombre')
    puntaje=models.IntegerField(default=0)
    idPista=models.CharField(max_length=20,default='0')
    codigo=models.ForeignKey(Partida,on_delete=models.CASCADE)
    
  
class Ranking(models.Model):
    idRanking=models.CharField(primary_key=True,max_length=200,default='0o0')
    codigo=models.ForeignKey(Partida,on_delete=models.CASCADE)

class Codigos(models.Model):
    cod=models.CharField(max_length=200, default='0j0')

class Comentarios(models.Model):
    idComentario= models.CharField(max_length=200, default='esto es un comentario')
    puntuacionUno= models.IntegerField(default=0)
    puntuacionDos= models.IntegerField(default=0)
    puntuacionTres= models.IntegerField(default=0)
