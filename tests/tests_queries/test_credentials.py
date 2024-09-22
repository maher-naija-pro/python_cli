from pytest import fixture
from neurodeploy import credentials
from tests.login import login


@fixture
def create_credential(login):
    credentials.create("test3", "fff")
    yield


def test_get_credential(login):
    assert credentials.get()


def test_create_credential(login):
    assert credentials.create("test3", "fff")


def test_delete_credential(create_credential):
    assert credentials.delete("test3") == {
        "message": "Deleted user somedude11's credential 'test3'.",
        "status_code": 200,
    }
