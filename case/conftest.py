from case.common_api.common_fuction import login
import requests
import pytest


@pytest.fixture(scope="session")
def login_fixture():
    s = requests.session()
    login(s, user="test2")  # s已经带token
    print("用例的前置操作")
    yield s
    print("用例结束之后只执行一次")


@pytest.fixture(scope="function")
def unlogin_fixture():
    s = requests.session()
    yield s
    print("每个用例都会执行一次")
