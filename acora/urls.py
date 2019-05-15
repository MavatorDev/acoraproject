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
from .views import CPartida
from django.http import HttpResponse

urlpatterns = [ 
        path('equiposPartida/<slug:foo>',equiposPartida.as_view(), name='equiposPartida'),
        path('crearPartida',crearPartida.as_view(), name='crearPartida'), 
        path('login/<slug:foo>',login.as_view(), name='login'),
        path('Clogin',Clogin.as_view(), name='Clogin'),
        path('iniciarPartida/<slug:foo>',iniciarPartida.as_view(), name='iniciarPartida'),
        path('actualizarPuntaje/<slug:foo>',actualizarPuntaje.as_view(), name='actualizarPuntaje'),
        path('finalizarPartida/<slug:foo>',finalizarPartida.as_view(), name='finalizarPartida'),
        path('getTemporizador/<slug:foo>',getTemporizador.as_view(), name='getTemporizador'),
        path('getRanking/<slug:foo>',getRanking.as_view(), name='getRanking'),
        path('CPartida/<slug:foo>',CPartida.as_view(), name='CPartida'),
        ]
	
