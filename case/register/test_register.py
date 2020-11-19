import pytest
from case.common_api.common_fuction import register



def test_register_1(unlogin_fixture, delete_user):
    '''注册成功'''
    s = unlogin_fixture
    r = register(s, username="test_123")
    print(r.text)
    assert r.json()["code"] == 0


def test_register_2(unlogin_fixture, delete_user):
    '''已经被注册'''
    s = unlogin_fixture
    r = register(s, username="test_123")
    print(r.text)
    assert r.json()["code"] == 0    # 第一次注册


    # 第二次  已被注册
    r2 = register(s, username="test_123")
    print(r2.text)
    assert r2.json()["code"] == 2000
    assert r2.json()["msg"] == "test_123用户已被注册"

