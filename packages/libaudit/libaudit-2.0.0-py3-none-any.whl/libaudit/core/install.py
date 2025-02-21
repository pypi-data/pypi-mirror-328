from typing import TYPE_CHECKING
from typing import Any
from typing import Optional
import pathlib

from .settings import get_excluded_tables
from .settings import get_handler_class


if TYPE_CHECKING:
    from typing import Tuple


class AuditInstaller:
    """Установщик процедур и триггеров журналирующих изменения."""

    def __init__(self):
        handler_cls = get_handler_class()
        self.handler = handler_cls()

    @staticmethod
    def _read_sql(filename):
        """Чтение sql из файла."""
        sql_file_path = pathlib.Path(__file__).parent / 'sql' / filename
        with sql_file_path.open(mode='r', encoding='utf-8') as sql_file:
            return sql_file.read()

    def get_install_sql(self) -> 'Tuple[tuple[str, Optional[Any]], ...]':
        """Набор запросов с параметрами, выполняющих установку."""
        excluded_tables = set(get_excluded_tables())
        excluded_tables.update(self.handler.excluded_tables)

        return (
            ('CREATE EXTENSION IF NOT EXISTS hstore;', None),
            # установка обработчика
            (self.handler.get_install_sql(), None),
            # Установка триггеров в таблицы
            (self._read_sql('apply_triggers.sql'), None),
            ('SELECT apply_triggers(%s);', (list(excluded_tables),)),
        )

    def get_uninstall_sql(self) -> 'Tuple[tuple[str, Optional[Any]], ...]':
        """Набор запросов с параметрами, выполняющих удаление."""
        return (
            (self._read_sql('remove_triggers.sql'), None),
            (self.handler.get_uninstall_sql(), None),
        )
