from rest_framework import serializers
from . import models
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nome', 'telefone', 'created_at','updated_at',)
        fields = '__all__'
        model = models.Cliente