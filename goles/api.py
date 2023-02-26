from .models import Goles
from rest_framework import viewsets, permissions
from .serializers import GolesSerializer

class GolesViewSet(viewsets.ModelViewSet):
    queryset = Goles.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GolesSerializer