import requests
from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager(logger_name="api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                                   log_filename="api.log",
                                                                   log_path=LOG_PATH)

def login(s, user="test1", psw="123456"):
    '''实现登录'''
    url = "http://49.235.92.12:6009/api/v1/login"

    body = {
        "username": user,
        "password": psw
    }
    r = s.post(url, json=body)
    logger.debug("登陆返回:%s"%r.text)
    # print(r.text)

    # 提取token
    token = r.json()["token"]
    logger.debug("获取token:%s"%token)
    # print(token)
    h = {
        "Authorization": "Token "+token
    }
    s.headers.update(h)  # s已经带了token

    return token


def get_info(s):
    '''获取个人信息'''
    url2 = "http://49.235.92.12:6009/api/v1/userinfo"
    r2 = s.get(url2)
    # print(r2.text)
    logger.debug("获取个人信息:%s"%r2.text)
    return r2


def modefy_info(s, name="test2", age=22, sex="M", mail="xxx@qq.com"):
    url2 = "http://49.235.92.12:6009/api/v1/userinfo"

    body = {"name": name,
            "age": age,
            "sex": sex,
            "mail": mail}
    r2 = s.post(url2, json=body)
    logger.debug("修改个人信息:%s"%r2.text)
    return r2

def register(s, username="test_123", password="123456"):
    '''注册接口'''
    url = "http://49.235.92.12:6009/api/v1/register"

    body = {
        "username": username,
        "password": password,
        "mail": "222222@qq.com"
        }
    r = s.post(url, json=body)
    logger.debug("注册接口返回:%s"%r.text)
    return r

if __name__ == '__main__':
    s = requests.session()
    r = register(s, username="test_123", password="123456")
    print(r.text)