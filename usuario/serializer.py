from rest_framework import serializers
from . import models
class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)
   
    class Meta:
        fields = '__all__'
        model = models.Usuario
'''
    def create(self, validated_data):
        user = super(UsuarioSerializer, self).create(validated_data)
        user.set_password(validated_data['senha'])
        user.save()
        return user'''
