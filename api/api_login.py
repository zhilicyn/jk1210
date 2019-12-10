# 导包
import requests

import api

class ApiLogin(object):
    # 初始化
    def __init__(self):
        self.url = api.BASE_URL+"/api/sys/login"

    # 登录
    def api_login(self,mobile,password):
        # 定义请求json数据
        data = {"mobile":mobile,"password":password}
        # 调用post方法,返回响应对象
        return requests.post(self.url,json=data,headers=api.headers)


if __name__ == '__main__':
    login = ApiLogin()
    print(login.api_login(mobile="13800000002",password="123456").json())