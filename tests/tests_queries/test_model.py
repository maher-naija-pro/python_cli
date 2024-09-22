from neurodeploy import model
from tests.login import login


def test_push_model_no_file(login):
    assert model.push("my_model") == {
        "message": "Your model params has been updated",
        "status_code": 200,
    }


def test_push_model_file(login):
    persistance_type = "h5"
    assert model.push("my_model", "./model.h5") == {
        "message": "Upload successful",
        "status_code": 200,
    }


def test_push_model_file_type(login):
    assert model.push("my_model", "./model.h5", "tensorflow", "h5") == {
        "message": "Upload successful",
        "status_code": 200,
    }


def test_push_model_file_false_type(login):
    result = model.push("my_model", "./model.h5", "tenorflow", "h5")
    assert "errors" in result


def test_list_model(login):
    assert model.list()


# @pytest.mark.skip(reason="no way of currently testing this")
def test_predict_model(login):
    model_name = "my_model"
    data = [[1, 2, 3, 4, 5]]
    assert model.predict(model_name, data) == {
        "output": [[9.991751670837402]],
        "status_code": 200,
    }


def test_delete_model(login):
    model_name = "my_model"
    assert model.delete(model_name) == {
        "message": "deleted model my_model",
        "status_code": 200,
    }
