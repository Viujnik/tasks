from dataclasses import dataclass


@dataclass
class Task:
    """Класс Task"""
    id: int
    type: str
    payload: dict
