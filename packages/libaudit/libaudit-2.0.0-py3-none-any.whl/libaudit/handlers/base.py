from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Tuple


class AbstractAuditLogHandler(ABC):
    """Абстрактный обработчик имзенений."""

    @abstractmethod
    def get_install_sql(self) -> str:
        """Возвращает SQL-функцию, которую должен вызывать триггер."""

    @abstractmethod
    def get_uninstall_sql(self) -> str:
        """Возвращает строку с SQL запросом удаляющем функцию, вызываемую триггером."""

    @property
    def excluded_tables(self) -> 'Tuple[str, ...]':
        """Список таблиц, вешать триггеры на которые не требуется."""
        return ()
