from rest_framework import serializers
from . import models

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Documento

