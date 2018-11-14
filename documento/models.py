from django.db import models

class Documento(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    data = models.CharField(max_length=15)
    autor = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    documento = models.FileField()
 
    
def __str__(self):
    return self.titulo