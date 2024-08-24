from django_filters import rest_framework as filters

from network.models import NetworkEntity


class NetworkEntityFilter(filters.FilterSet):
    country = filters.CharFilter(field_name='contacts__country', lookup_expr='iexact')

    class Meta:
        model = NetworkEntity
        fields = ['country']
