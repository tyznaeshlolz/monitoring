from rest_framework import viewsets
from .serializers import GateSerializer, OSUserSerializer
from .models import Gate, OSUser


class OSUserViewSet(viewsets.ModelViewSet):
    serializer_class = OSUserSerializer
    queryset = OSUser.objects.all()


class GateViewSet(viewsets.ModelViewSet):
    serializer_class = GateSerializer
    queryset = Gate.objects.all()
