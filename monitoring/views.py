import logging

from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import GateSerializer, OSUserSerializer, VisitLogSerializer
from .models import Gate, OSUser, VisitLog


logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)


class OSUserViewSet(viewsets.ModelViewSet):
    serializer_class = OSUserSerializer
    queryset = OSUser.objects.all()


class GateViewSet(viewsets.ModelViewSet):
    serializer_class = GateSerializer
    queryset = Gate.objects.all()


class VisitLogViewSet(viewsets.ViewSet):
    queryset = VisitLog.objects.all()
    serializer_class = VisitLogSerializer

    @transaction.atomic
    def create(self, request):
        try:
            user_id = request.data['user_id']
            gate_id = request.data['gate_id']
            pass_number = request.data['pass_number']
            user = OSUser.objects.get(id=user_id)
            gate = Gate.objects.get(id=gate_id)

            if user.pass_number != pass_number:
                logger.error('Неверный номер пропуска пользователя')
                return Response({'error': 'Неверный номер пропуска'},
                                status=status.HTTP_400_BAD_REQUEST)

            user.at_work = not user.at_work
            user.save()

            visit = VisitLog.objects.create(user=user,
                                            user_status=user.at_work,
                                            gate=gate,
                                            pass_number=pass_number)

            serializer = VisitLogSerializer(visit)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except OSUser.DoesNotExist:
            logger.error('Пользователь не найден')
            return Response({'error': 'Пользователь не найден'},
                            status=status.HTTP_400_BAD_REQUEST)

        except Gate.DoesNotExist:
            logger.error('КПП не найден')
            return Response({'error': 'КПП не найден'},
                            status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        serializer = VisitLogSerializer(VisitLog.objects.all(), many=True)
        return Response(serializer.data)
