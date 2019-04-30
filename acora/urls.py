from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
       
       path('Clogin/',views.Clogin, name='Clogin'),
       path('login/<slug:foo>',views.login, name='login'),
       path('lobby/',views.lobby, name='lobby'),
       path('crearEquipo/<int:pk>',views.crearEquipo, name='crearEquipo'),
       path('iniciarPartida/<int:pk>',views.iniciarPartida, name='iniciarPartida'),
       path('actualizarPuntaje/<slug:foo>',views.actualizarPuntaje, name='actualizarPuntaje'),
       path('finalizarPartida/<int:pk>',views.finalizarPartida, name='finalizarPartida'),
       path('getEquiposPartida/<int:pk>',views.getEquiposPartida, name='getEquiposPartida'),
       path('getTemporizador/<int:pk>',views.getTemporizador, name='getTemporizador'),
       path('getRanking/<int:pk>',views.getRanking, name='getRanking'),
]
	