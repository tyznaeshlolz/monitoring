from rest_framework import viewsets
from .serializers import OSUserSerializer
from .models import OSUser


class OSUserViewSet(viewsets.ModelViewSet):
    serializer_class = OSUserSerializer
    queryset = OSUser.objects.all()