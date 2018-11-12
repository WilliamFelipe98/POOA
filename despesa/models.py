from django.db import models

class Despesa(models.Model):
    descricao = models.CharField(max_length=50)
    usuario = models.CharField(max_length=10)
    valor = models.CharField(max_length=20)
    data = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
def __str__(self):
    return self.descricao