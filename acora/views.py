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

    def get(self,request,foo):
        equipos = Equipo.objects.filter(codigo=foo).values_list('cod','nombre')
        equipos = list(equipos)
             
        return Response(equipos)

    def post(self,request,foo):
        serializer=PostcEquipo(data=request.data)
        if serializer.is_valid():
           if Partida.objects.filter(codigo=foo).exists():
               if Equipo.objects.filter(codigo=foo, nombre=request.data["nombre"]).exists():
                   return Response("nombreExiste")
               else:
                  foo=get_object_or_404(Partida, codigo=foo)
                  serializer.save(codigo=foo)  
                  return Response("aceptado")
           else: 
            return Response("codigoFail")
        else:
            return Response("unknownFail")

class crearPartida(APIView):
 
     def post(self,request):
         serializer=sPartida(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response("aceptado")
         else:
            return Response("unknownFail")

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

    def post(self,request,foo):
     if (Partida.objects.filter(codigo=foo)).exists():
      dato=get_object_or_404(Partida, codigo=foo)
      dato.temporizador=request.data
      return Response("aceptado")
     else:
      return Response("rechazado")

class CPartida(APIView):
    def get(self,request,foo):
        if (Partida.objects.filter(codigo=foo)).exists():
            return Response("aceptado")
        else:
            return Response("rechazado")

class actualizarPuntaje(APIView):
     
    def post(self,request,foo):
     
     if (Equipo.objects.filter(cod=foo)).exists():
      dato=get_object_or_404(Equipo, cod=foo)
       
      serializer=PostAPuntaje(data=request.data,instance=dato)
      if serializer.is_valid():
             
            serializer.save(puntaje= request.data["puntaje"])
      
            return Response("aceptado")
     else:
      return Response("rechazado")

class finalizarPartida(APIView):
   
    def get(self,request,foo):
     if (Partida.objects.filter(codigo=foo)).exists(): 
      u=Partida.objects.get(codigo=foo).delete()
      return Response("aceptado")
     else:
      return Response("rechazado")

class getTemporizador(APIView):

    def get(self,request,foo):
     if (Partida.objects.filter(codigo=foo)).exists(): 
      dato=Partida.objects.get(codigo=foo).temporizador
      return Response(dato)
     else:
      return Response("rechazado")

class getRanking(APIView):

    def get(self,request,foo):
      if (Partida.objects.filter(codigo=foo)).exists():
       equipos= Equipo.objects.filter(codigo=foo).order_by('-puntaje').values_list('cod','nombre','puntaje')
       equipos=list(equipos) 
       return Response(equipos)
      else:
       return Response("rechazado")
