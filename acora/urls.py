from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
       
       path('login/',views.login, name='login'),
       path('lobby/',views.lobby, name='lobby'),
       path('crearEquipo/<int:pk>',views.crearEquipo, name='crearEquipo'),
       path('iniciarPartida/<int:pk>',views.iniciarPartida, name='iniciarPartida'),
       path('actualizarPuntaje/<slug:foo>',views.actualizarPuntaje, name='actualizarPuntaje'),
       path('finalizarPartida/<int:pk>',views.finalizarPartida, name='finalizarPartida'),
]
	