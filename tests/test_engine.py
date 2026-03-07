from src.main import give_engine

class TestSimulation:
    def test_simulator_engine(self, mocker):
        """
        Тестирует, что в main'е функция выводит ровно 3 вида по 5 task'ов.
        """
        mocker.patch("builtins.input", return_value="test_command")
        mock_print = mocker.patch("builtins.print")

        give_engine()

        assert mock_print.call_count == 15
