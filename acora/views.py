from django.http import JsonResponse
from rest_framework import generics
from .models import Equipo
from .models import Partida
from .models import Codigos
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import sPartida
from .serializers import PostcEquipo
from .serializers import PostIPartida
from .serializers import PostAPuntaje
from .serializers import PostCodigos

class equiposPartida(APIView):

    def get(self,request,pk):
        equipos = Equipo.objects.filter(codigo=pk).values_list('cod','nombre')
        equipos = list(equipos)
             
        return Response(equipos)

    def post(self,request,pk):
        serializer=PostcEquipo(data=request.data)
        if serializer.is_valid():
           pk=get_object_or_404(Partida, codigo=pk)
           serializer.save(codigo=pk)     
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class crearPartida(APIView):
 
     def post(self,request):
         serializer=sPartida(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
     
     def get(self,request,foo):
       if Codigos.objects.filter(cod=foo).exists():
        return Response("aceptado")
       else:
        return Response("rechazado")

class Clogin(APIView):
  
     def post(self,request):
       serializer=PostCodigos(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class iniciarPartida(APIView):

    def post(self,request,pk):
     if (Partida.objects.filter(codigo=pk)).exists():
      dato=get_object_or_404(Partida, codigo=pk)
      dato.temporizador=request.data
      return Response("empezar")
     else:
      return Response("rechazado")

class CPartida(APIView):
    def get(self,request,pk):
        if (Partida.objects.filter(codigo=pk)).exists():
            return Response("aceptado")
        else:
            return Response("rechazado")

class actualizarPuntaje(APIView):
     
    def post(self,request,foo):
     
     if (Equipo.objects.filter(nombre=foo)).exists():
      dato=get_object_or_404(Equipo, nombre=foo)
       
      serializer=PostAPuntaje(data=request.data,instance=dato)
      if serializer.is_valid():
             
            serializer.save(puntaje=Equipo.objects.get(nombre=foo).puntaje + request.data["puntaje"])
      
            return Response("aceptado")
     else:
      return Response("rechazado")

class finalizarPartida(APIView):
   
    def get(self,request,pk):
     if (Partida.objects.filter(codigo=pk)).exists(): 
      u=Partida.objects.get(codigo=pk).delete()
      return Response("eliminado")
     else:
      return Response("rechazado")

class getTemporizador(APIView):

    def get(self,request,pk):
     if (Partida.objects.filter(codigo=pk)).exists(): 
      dato=Partida.objects.get(codigo=pk).temporizador
      return Response(dato)
     else:
      return Response("rechazado")

class getRanking(APIView):

    def get(self,request,pk):
      if (Partida.objects.filter(codigo=pk)).exists():
       equipos= Equipo.objects.filter(codigo=pk).order_by('-puntaje').values_list('cod','nombre','puntaje')
       equipos=list(equipos) 
       return Response(equipos)
      else:
       return Response("rechazado")
