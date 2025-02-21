from rest_framework.fields import CharField
from rest_framework.fields import IntegerField
from rest_framework.fields import JSONField
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer

from libaudit.core.types import OperationType
from libaudit.handlers.database_table.proxies import AuditLogViewProxy


class OperationSerializer(Serializer):
    """Сериалайзер данных об операции."""

    id = IntegerField(read_only=True, source='value')
    name = CharField(read_only=True, source='label')

    def to_representation(self, instance):  # noqa: D102
        return super().to_representation(instance)


class AuditLogSerializer(ModelSerializer):
    """Сериалайзер данных записи журнала изменений."""

    user_name = CharField(read_only=True)
    model_verbose_name = CharField(read_only=True)
    diff = JSONField(read_only=True)
    operation = OperationSerializer(read_only=True)

    def to_representation(self, instance):  # noqa: D102
        instance.operation = next(i for i in OperationType if i.value == instance.operation)
        return super().to_representation(instance)

    class Meta:  # noqa: D106
        model = AuditLogViewProxy
        fields = (
            'id',
            'model_verbose_name',
            'user_name',
            'diff',
            'user_id',
            'user_type_id',
            'timestamp',
            'table_name',
            'old_data',
            'changes',
            'operation',
            'request_id',
            'transaction_id',
            'ip_address',
        )
