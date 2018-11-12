from django.shortcuts import render
from rest_framework import generics
from .models import Noticia
from .serializer import NoticiaSerializer

class NoticiaList(generics.ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class NoticiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


