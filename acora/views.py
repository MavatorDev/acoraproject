from django.shortcuts import render, get_object_or_404
from .models import Equipo
from .models import Codigos
from .models import Partida
from django.http import HttpResponse
from .forms import PostCodigos
from .forms import PostLobby
from .forms import PostcEquipo
from .forms import PostIPartida
from .forms import PostAPuntaje
#crear vistas



def login(request):   
  if request.method == "POST":
      form = PostCodigos(request.POST)
      if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return HttpResponse("sidio")
  else:
      form = PostCodigos()
      return render(request, 'acora/login.html', {'form': form})


def lobby(request):   
  if request.method == "POST":
      form = PostLobby(request.POST)
      if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return HttpResponse("sidio")
  else:
      form = PostLobby()
      return render(request, 'acora/lobby.html', {'form': form})

def crearEquipo(request,pk):      
    
    if request.method == "POST":
       form = PostcEquipo(request.POST)
     
       if form.is_valid():
        post = form.save(commit=False)
        post.codigo=get_object_or_404(Partida, codigo=pk)
        post.save()
        return HttpResponse("sidio")
    else:
      form = PostLobby()
      return render(request, 'acora/crearEquipo.html', {'form': form})

def iniciarPartida(request,pk):      
    post = get_object_or_404(Partida, codigo=pk)
    if request.method == "POST":
       form = PostIPartida(request.POST)
     
       if form.is_valid():
        post = form.save(commit=False)
        
        post.save()
        return HttpResponse("sidio")
    else:
      form = PostLobby()
      return render(request, 'acora/iniciarPartida.html', {'form': form})

def actualizarPuntaje(request,foo):      
    post = get_object_or_404(Equipo, nombre=foo)
    if request.method == "POST":
       form = PostAPuntaje(request.POST,instance=post)
       
       if form.is_valid():
        post = form.save(commit=False)
        post.puntaje= Equipo.objects.get(nombre=foo).puntaje + int(request.POST['puntaje'])
        post.save()
        return HttpResponse("sidio")
    else:
      form = PostLobby()
      return render(request, 'acora/actualizarPuntaje.html', {'form': form})

def finalizarPartida(request,pk):
   u=Partida.objects.get(codigo=pk).delete()
   return HttpResponse("sidio")