import random
from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@dataclass
class Task:
    """Класс Task"""
    id: int
    type: str
    payload: dict


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


class FileSource:
    def get_tasks(self) -> list[Task]:
        tasks_list = []
        for i in range(5):
            tasks_list.append(Task(id=random.randint(1000, 9999), type="file",
                                   payload={"sender_id": random.randint(100000, 999999),
                                            "receiver_id": random.randint(100000, 999999),
                                            "filename": f"pron_{random.randint(100, 999)}_{random.randint(10, 99)}.mp4",
                                            "file_size": random.randint(1000, 9999)}))
        return tasks_list

    def printf_task(self, task: Task):
        return f"ID: {task.id}\tTask type: {task.type}\nUser({task.payload["sender_id"]}) send file {task.payload["filename"]}({task.payload["file_size"]} MB) to {task.payload["receiver_id"]}\n"


class ConsoleSource:
    def get_tasks(self) -> list[Task]:
        tasks_list = []
        for i in range(5):
            tasks_list.append(Task(id=random.randint(1000, 9999), type="console",
                                   payload={"sender_id": random.randint(100000, 999999),
                                            "command": input("Введите команду системы: "),
                                            "status": random.choice(["OK", "ERROR", "WARNING", "CRITICAL"])}))
        return tasks_list

    def printf_task(self, task: Task):
        return f"ID: {task.id}\tTask type: {task.type}\nUser({task.payload["sender_id"]}) send command {task.payload["command"]})\nResponse status: {task.payload["status"]}\n"


class APISource:
    def get_tasks(self) -> list[Task]:
        tasks_list = []
        for i in range(5):
            tasks_list.append(Task(id=random.randint(1000, 9999), type="api",
                                   payload={"client_id": random.randint(100000, 999999),
                                            "HTTP_METHOD": random.choice(["GET", "POST", "PUT", "PATCH"]),
                                            "url": "https://rkn.gov.ru", "status_code": "ERROR"}))
        return tasks_list

    def printf_task(self, task: Task):
        return f"ID: {task.id}\tTask type: {task.type}\nClient({task.payload["client_id"]}) send {task.payload["HTTP_METHOD"]} request to {task.payload["url"]}.\nResponse status: {task.payload["status_code"]}\n"
