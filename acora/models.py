from django.db import models
from django.utils import timezone

class Equipo(models.Model):
   # id=models.CharField(max_length=200)
    puntaje=models.IntegerField(default=0)
   # timer= models.TimeField(default='00:00')
    codigo=models.CharField(max_length=200)

class Partida(models.Model):
    codigo= models.CharField(max_length=200)

class Pista(models.Model):
   # id=models.CharField(max_length=200)
    Actividad=models.CharField(max_length=300)

class Ranking(models.Model):
   # id=models.CharField(max_length=20)
    codigo=models.CharField(max_length=29)



# def getTime(self):
 #       self.timer = time.now()
  #      self.save()

#def getpuntaje(self):
 #   return self.puntaje
