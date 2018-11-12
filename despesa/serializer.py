from rest_framework import serializers
from . import models
class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'descricao', 'valor', 'created_at','updated_at',)
        fields = '__all__'
        model = models.Despesa