from django.shortcuts import render

from rest_framework import generics
from .models import Despesa
from .serializer import DespesaSerializer
from rest_framework.permissions import IsAuthenticated

class DespesaList(generics.ListCreateAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    permission_classes = (IsAuthenticated,)
    
class DespesaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    permission_classes = (IsAuthenticated,)