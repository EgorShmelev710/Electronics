from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.filters import NetworkEntityFilter
from network.models import NetworkEntity
from network.serializers import NetworkEntitySerializer


class NetworkEntityViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkEntitySerializer
    queryset = NetworkEntity.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NetworkEntityFilter
