from neurodeploy import user
from tests.login import delete_nd_after


def test_login(delete_nd_after):
    username = "somedude11"
    password = "Password1234"
    assert user.login(username, password) == {
        "message": "Your token is saved",
        "status_code": 200,
    }
