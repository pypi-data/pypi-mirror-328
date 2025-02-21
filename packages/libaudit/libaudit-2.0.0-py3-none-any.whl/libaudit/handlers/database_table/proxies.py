from functools import cached_property

from django.apps import apps
from django.db.models import BooleanField
from django.db.models import IntegerField
from django.db.models.fields.related import RelatedField
from django.utils.encoding import force_str

from libaudit.core.types import OperationType

from .models import AuditLog


class ModelRegistry:
    """Реестр моделей в системе."""

    @cached_property
    def table_model(self):
        """Сопоставление имён таблиц с моделями."""
        return {
            model._meta.db_table: model
            for model in apps.get_models(include_auto_created=True)
            if not (model._meta.proxy)
        }

    def get_model(self, table_name: str):
        """Возвращает класс модели по имени таблицы."""
        return self.table_model.get(table_name)


model_registry = ModelRegistry()


class AuditLogViewProxy(AuditLog):
    """Прокси-модель для отображения."""

    class Meta:  # noqa: D106
        proxy = True

    @property
    def model(self):
        """Класс измененной модели."""
        return model_registry.get_model(self.table_name)

    @property
    def fields(self):
        """Все поля измененной модели.

        :returns dict: {имя колонки в БД: поле, ...}
        """
        model = self.model
        if model:
            result = {field.get_attname_column()[1]: field for field in model._meta.fields}
            return result

    @property
    def model_verbose_name(self):
        """Отображаемое имя модели."""
        model = self.model
        if model:
            return model._meta.verbose_name
        return self.table_name

    @property
    def diff(self):
        """Возвращает diff для объекта.

        :return: list[dict]: Словари, с ключами "name", "old", "new", где:
            "name" - verbose_name поля модели, если удалось определить,
                     иначе его имя,
            "old" и "new" - старое и новое значение поля соответственно.
        """
        empty = {}

        if self.operation == OperationType.INSERT:
            keys = self.changes.keys()
            data = empty
            new_data = self.changes or empty
        elif self.operation == OperationType.UPDATE:
            keys = self.changes.keys()
            data = self.old_data or empty
            new_data = self.changes or empty
        elif self.operation == OperationType.DELETE:
            keys = self.old_data.keys()
            data = self.old_data or empty
            new_data = empty
        else:
            keys = data = new_data = empty

        result = [
            {
                'name': key,
                'verbose_name': self.get_field_string(key),
                'old': self.convert_field_value(key, data.get(key, '')),
                'new': self.convert_field_value(key, new_data.get(key, '')),
            }
            for key in keys
        ]
        result.sort(key=lambda x: x['name'])

        return result

    def get_field_string(self, column_name: str):
        """Возвращает отображаемое имя поля модели.

        :param str column_name: имя столбца в БД.
        :return str: verbose_name столбца, если есть, иначе column_name.
        """
        name = column_name
        if self.fields:
            field = self.fields.get(column_name)
            if field and field.verbose_name:
                name = force_str(field.verbose_name)
        return name

    def convert_field_value(self, column_name: str, value):
        """Возвращает значение поля."""

        def get_choice(choices, choice_id):
            if choice_id:
                choice_id = int(choice_id)
            return dict(choices).get(choice_id, choice_id)

        if value is None:
            return ''

        if self.fields:
            field = self.fields.get(column_name)
            if field:
                try:
                    if isinstance(field, RelatedField):
                        if value:
                            related = field.remote_field
                            model = related.model
                            field_name = related.field_name
                            qs = model._default_manager.filter(**{field_name: value})[:1]
                            if qs:
                                value = '{{{}}} {}'.format(
                                    qs[0].id,
                                    self._get_object_verbose_name(qs[0]),
                                )
                    elif isinstance(field, BooleanField):
                        value_map = {'t': True, 'f': False}
                        value = value_map.get(value, value)
                    elif isinstance(field, IntegerField) and field.choices:
                        value = get_choice(field.choices, value)
                except (ValueError, TypeError):
                    pass
        return force_str(value)

    @staticmethod
    def _get_object_verbose_name(instance):
        """Возвращает отображаемое значение в str для инстанса модели."""
        # pylint: disable=broad-except

        if hasattr(instance, 'log_display'):
            try:
                return instance.log_display()
            except Exception:  # noqa: S110
                pass
        elif hasattr(instance, 'display'):
            try:
                return instance.display()
            except Exception:  # noqa: S110
                pass
        return str(instance)
