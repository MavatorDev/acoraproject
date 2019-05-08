from django.urls import path
from . views import equiposPartida
from . views import crearPartida
from . views import login
from . views import Clogin
from . views import iniciarPartida
from .views import actualizarPuntaje
from .views import finalizarPartida
from .views import getTemporizador
from .views import getRanking
from django.http import HttpResponse

urlpatterns = [ 
        path('equiposPartida/<int:pk>',equiposPartida.as_view(), name='equiposPartida'),
        path('crearPartida',crearPartida.as_view(), name='crearPartida'), 
        path('login/<slug:foo>',login.as_view(), name='login'),
        path('Clogin',Clogin.as_view(), name='Clogin'),
        path('iniciarPartida/<int:pk>',iniciarPartida.as_view(), name='iniciarPartida'),
        path('actualizarPuntaje/<slug:foo>',actualizarPuntaje.as_view(), name='actualizarPuntaje'),
        path('finalizarPartida/<int:pk>',finalizarPartida.as_view(), name='finalizarPartida'),
        path('getTemporizador/<int:pk>',getTemporizador.as_view(), name='getTemporizador'),
        path('getRanking/<int:pk>',getRanking.as_view(), name='getRanking'),
      ]
	
