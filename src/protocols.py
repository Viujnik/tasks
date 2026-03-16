from typing import runtime_checkable, Protocol

from src.sources import Task


@runtime_checkable
class TasksGiver(Protocol):
    """
    Контракт для источников task'ов.
    """

    def get_tasks(self) -> list[Task]:
        """
        Создает список из 5 task'ов соответствующего вида, созданных заранее.
        """
        pass
    def printf_task(self, task: Task) -> None:
        """
        Выводит форматированную информацию task'и.
        """
        pass
