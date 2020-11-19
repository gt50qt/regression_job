'''实现登录'''
url = "http://49.235.92.12:6009/api/v1/login"

body = {
    "username": username,
    "password": username
}
r = s.post(url, json=body)

# print(r.text)

# 提取token
token = r.json()["token"]
logger.debug("获取token:%s" % token)
# print(token)
h = {
    "Authorization": "Token " + token
}
s.headers.update(h)  # s已经带了token
