import os, shutil
from pytest import fixture
from neurodeploy import user

HOME = os.path.expanduser("~")


@fixture
def login():
    username = "somedude11"
    password = "Password1234"
    user.login(username, password)
    yield
    # command to delete whatever
    shutil.rmtree(f"{HOME}/.nd")


@fixture
def delete_nd_after():
    yield
    # command to delete whatever
    shutil.rmtree(f"{HOME}/.nd")
