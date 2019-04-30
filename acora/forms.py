from django import forms
from .models import Codigos
from .models import Partida
from .models import Equipo

class PostCodigos(forms.ModelForm):
   
   class Meta:
        model = Codigos
        fields = ('cod',)
   
class PostLobby(forms.ModelForm):
   class Meta:
        model = Partida
        fields = ('codigo','estado', 'temporizador',)

class PostcEquipo(forms.ModelForm):
   class Meta:
        model = Equipo
        fields = ('cod','nombre','puntaje','idPista',)

class PostIPartida(forms.ModelForm):
   class Meta:
        model = Partida
        fields = ('temporizador',)

class PostAPuntaje(forms.ModelForm):
   class Meta:
        model = Equipo
        fields = ('puntaje',)

