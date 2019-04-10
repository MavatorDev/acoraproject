from django.db import models
from django.utils import timezone

class Equipo(models.Model):
    ide=models.CharField(max_length=200)
    puntaje=models.IntegerField(default=0)
    timer= models.TimeField(default='00:00')
    
def getTime(self):
        self.timer = time.now()
        self.save()

def getpuntaje(self):
    return self.puntaje
