from django.shortcuts import render
from rest_framework import generics
from .models import Noticia
from .serializer import NoticiaSerializer
from rest_framework.permissions import IsAuthenticated

class NoticiaList(generics.ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = (IsAuthenticated,)

class NoticiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = (IsAuthenticated,)


