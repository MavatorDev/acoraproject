from rest_framework import serializers
from .models import Codigos
from .models import Partida
from .models import Equipo

class sPartida(serializers.ModelSerializer):
     class Meta:
         model= Partida
         fields=('codigo','estado','temporizador')

class PostCodigos(serializers.ModelSerializer):
   
   class Meta:
        model = Codigos
        fields = ('cod',)

class PostcEquipo(serializers.ModelSerializer):
   class Meta:
        model = Equipo
        fields = ('cod','nombre','puntaje','idPista',)

class PostIPartida(serializers.ModelSerializer):
   class Meta:
        model = Partida
        fields = ('temporizador',)

class PostAPuntaje(serializers.ModelSerializer):
   class Meta:
        model = Equipo
        fields = ('puntaje',)