from typer.testing import CliRunner
from procurement_tools.cli.main import app

runner = CliRunner()


def test_app(sam_api_results):
    result = runner.invoke(app, ["sam", "XRVFU3YRA2U5"])
    assert result.exit_code == 0
    assert "JAMES & ENYART" in result.stdout
