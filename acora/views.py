from django.shortcuts import render
from .models import Equipo
#crear vistas

def post_list(request):
    equipos= Equipo.objects.order_by('puntaje')
    return render(request, 'acora/post_list.html',{'equipos': equipos})


