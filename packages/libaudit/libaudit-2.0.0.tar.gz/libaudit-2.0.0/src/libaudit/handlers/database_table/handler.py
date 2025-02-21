import pathlib

from ..base import AbstractAuditLogHandler
from .constants import AUDIT_LOG_TABLE_NAME


class AuditLogHandler(AbstractAuditLogHandler):
    """Обработчик с выводом изменений в таблицу."""

    @property
    def excluded_tables(self) -> tuple[str, ...]:
        """Вешать триггеры на таблицу с журналом операций не нужно."""
        return (AUDIT_LOG_TABLE_NAME,)

    def get_install_sql(self) -> str:
        """Возвращает SQL-процедуру, которую должен вызывать триггер."""
        sql_file_path = pathlib.Path(__file__).parent / 'sql' / 'handler.sql'
        with sql_file_path.open(mode='r', encoding='utf-8') as sql_file:
            sql = sql_file.read().replace('%AUDIT_LOG_TABLE_NAME%', AUDIT_LOG_TABLE_NAME)

        return sql

    def get_uninstall_sql(self) -> str:
        """Возвращает SQL запрос удаления функции обработчика логирования изменений."""
        return 'DROP FUNCTION IF EXISTS audit_handler;'
