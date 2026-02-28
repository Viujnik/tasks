from src.main import give_engine

class TestSimulation:
    def test_simulator_engine(self, mocker):
        mocker.patch("builtins.input", return_value="test_command")
        mock_print = mocker.patch("builtins.print")

        give_engine()

        assert mock_print.call_count == 15
