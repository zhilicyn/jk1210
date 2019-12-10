import requests

import api
from api.api_login import ApiLogin


class ApiEmployee:
    # 初始化
    def __init__(self):
        # 添加员工url
        self.url_add = api.BASE_URL + "/api/sys/user"
        # 员工其他操作通用url  {}是占位符
        self.url_emp = api.BASE_URL + "/api/sys/user/{}"

    # 添加员工
    def api_post_employee(self,username,mobile,workNum):
        # 定义json数据
        data = {"username": username,
                "mobile": mobile,
                "workNumber": workNum}
        return requests.post(url=self.url_add,json=data,headers=api.headers)

    # 修改员工
    def api_put_employee(self,username):
        data={"username":username}
        return requests.put(url=self.url_emp.format(api.user_id),json=data,headers=api.headers)

    # 查询员工
    def api_get_employee(self):
        return requests.get(url=self.url_emp.format(api.user_id),headers=api.headers)

    # 删除员工
    def api_delete_employee(self):
        return requests.delete(url=self.url_emp.format(api.user_id),headers=api.headers)


if __name__ == '__main__':
    login = ApiLogin()
    r_login = login.api_login(mobile="13800000002", password="123456")
    print(r_login.json())
    token = r_login.json().get("data")
    api.headers["Authorization"] = "Bearer "+token
    emp = ApiEmployee()

    r = emp.api_post_employee("shizhiliya","18772821112","12342")
    print(r.text)