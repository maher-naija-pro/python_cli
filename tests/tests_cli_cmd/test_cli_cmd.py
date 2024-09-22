from typer.testing import CliRunner
from neuro import app
from tests.login import login, delete_nd_after

runner = CliRunner()


def test_cli_cmd_login(delete_nd_after):
    result = runner.invoke(
        app,
        ["login", "--username", "somedude11", "--password", "Password1234"],
    )
    assert "Login Successful" in result.stdout


def test_cli_cmd_push_model(login):
    result = runner.invoke(
        app,
        [
            "model",
            "push",
            "--name",
            "maher",
            "--filepath",
            "model.h5",
            "--lib",
            "tensorflow",
            "--filetype",
            "h5",
        ],
    )
    assert "{'message': 'Upload successful', 'status_code': 200}" in result.stdout


def test_cli_cmd_predict_model(login):
    result = runner.invoke(
        app,
        [
            "model",
            "predict",
            "--name",
            "maher",
            "--data",
            "[[1, 2, 3, 4, 5]]",
        ],
    )
    assert "'output': [[9.991751670837402]]" in str(result.stdout)


def test_cli_cmd_delete_model(login):
    result = runner.invoke(
        app,
        ["model", "delete", "--name", "maher"],
    )
    assert "{'message': 'deleted model maher', 'status_code': 200}" in result.stdout


def test_cli_cmd_predict_no_model(login):
    result = runner.invoke(
        app,
        [
            "model",
            "predict",
            "--name",
            "maher",
            "--data",
            "[[1, 2, 3, 4, 5]]",
        ],
    )
    assert "" in str(result.stdout)


def test_cli_cmd_list_model(login):
    result = runner.invoke(app, ["model", "list"])
    assert "'models': []" in str(result.stdout)
