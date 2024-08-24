from rest_framework import serializers

from network.models import NetworkEntity


class NetworkEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkEntity
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'debt' in validated_data:
            raise serializers.ValidationError("Обнуление задолженности (обновление поля 'debt') запрещено.")

        return super().update(instance, validated_data)
