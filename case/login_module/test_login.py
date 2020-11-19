from case.common_api.common_fuction import login
import requests

def  test_login_success():
    '''输入正确账号，正确密码'''
    s = requests.session()
    token = login(s, user="test2", psw="123456")
    assert token


def  test_login_fail():
    '''输入正确账号，错误密码'''
    s = requests.session()
    token = login(s, user="test2", psw="1234561")
    assert not token

