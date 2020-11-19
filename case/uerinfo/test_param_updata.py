import requests
from case.common_api.common_fuction import login, modefy_info
import pytest
from common.read_yaml import read_yaml_data
import os
# 分离测试数据
# testdata = [
#                  [{"sex": "M", "age": 10, "mail": "111@qq.com"}, {"code": 0, "message": "update some data!"}],
#                  [{"sex": "F", "age": 10, "mail": "111@qq.com"}, {"code": 0, "message": "update some data!"}],
#                  [{"sex": "F", "age": 80, "mail": "111@qq.com"}, {"code": 0, "message": "update some data!"}],
#              ]
from setting import base_dir

yaml_path = os.path.join(base_dir, "testdata", "test_data.yml")
testdata = read_yaml_data(yaml_path)["test_param_updata"]



@pytest.mark.info
@pytest.mark.parametrize("test_input, expected", testdata)
def test_modefy_info_4(login_fixture, test_input, expected):
    '''登录-修改'''
    s = login_fixture
    r = modefy_info(s, sex=test_input["sex"], age=test_input["age"])
    print(r.text)
    assert r.json()["code"] == expected["code"]
    assert r.json()["message"] == expected["message"]
