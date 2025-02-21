import pathlib

from libaudit.handlers.base import AbstractAuditLogHandler


class AuditLogHandler(AbstractAuditLogHandler):
    """Обработчик с выводом изменений в стандартный вывод СУБД."""

    def get_install_sql(self) -> str:
        """Возвращает SQL-процедуру, которую должен вызывать триггер."""
        sql_file_path = pathlib.Path(__file__).parent / 'sql' / 'handler.sql'
        with sql_file_path.open(mode='r', encoding='utf-8') as sql_file:
            sql = sql_file.read()

        return sql

    def get_uninstall_sql(self) -> str:
        """Возвращает SQL запрос удаления функции обработчика логирования изменений."""
        return 'DROP FUNCTION IF EXISTS audit_handler;'
