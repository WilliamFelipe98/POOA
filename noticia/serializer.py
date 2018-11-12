from rest_framework import serializers
from . import models
class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'titulo', 'autor', 'created_at','updated_at','imagem')
        fields = '__all__'
        model = models.Noticia

