from rest_framework import serializers
from .models import Goles

class GolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goles
        fields = ('id', 'fecha', 'hora', 'equipo', 'rival', 'minuto', 'parcial')
        