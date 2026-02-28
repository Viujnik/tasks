import pytest

from src.models import FileSource, ConsoleSource, APISource, TasksGiver, Task

SOURCES = [FileSource, ConsoleSource, APISource]


class TestSourceStructure:
    @pytest.mark.parametrize("source_class", SOURCES)
    def test_get_tasks(self, source_class, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "test_command")
        source = source_class()
        tasks = source.get_tasks()
        assert isinstance(source, TasksGiver)
        assert all(isinstance(task, Task) for task in tasks)

    def test_api_source_printf(self):
        source = APISource()
        task = Task(id=1, type="api", payload={
            "client_id": 123, "HTTP_METHOD": "GET",
            "url": "https://test.com", "status_code": "OK"
        })
        output = source.printf_task(task)

        assert "ID: 1" in output
        assert "GET" in output
        assert "https://test.com" in output

    def test_file_source_printf(self):
        source = FileSource()
        task = Task(id=777, type="file", payload={
            "sender_id": 111,
            "receiver_id": 222,
            "filename": "test_document.pdf",
            "file_size": 500
        })
        output = source.printf_task(task)

        assert "ID: 777" in output
        assert "User(111)" in output
        assert "test_document.pdf" in output
        assert "500 MB" in output
        assert "222" in output

    def test_console_source_printf(self):
        source = ConsoleSource()
        task = Task(id=999, type="console", payload={
            "sender_id": 444,
            "command": "sudo rm -rf /",
            "status": "CRITICAL"
        })
        output = source.printf_task(task)

        assert "ID: 999" in output
        assert "User(444)" in output
        assert "sudo rm -rf /" in output
        assert "CRITICAL" in output
