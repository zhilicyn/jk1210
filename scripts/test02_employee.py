import unittest

from parameterized import parameterized

import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
from tools.read_txt import read_txt


class TestEmployee(unittest.TestCase):

    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取ApiEmployee对象
        cls.emp = ApiEmployee()


    # 新增员工
    @parameterized.expand(read_txt("employee_post.txt"))
    def test01_post(self,username,mobile,workNum):
        # 调用新增接口
        r = self.emp.api_post_employee(username,mobile,workNum)
        # 提取user_id
        print("添加员工响应结果为:",r.json())
        api.user_id = r.json().get("data").get("id")
        print("添加员工成功后id值为:",api.user_id)
        # 断言
        assert_common(self,r)

    # 修改员工
    def test02_put(self,username="shizhiliya"):
        # 调用更新接口方法
        # data={"username":username}
        r = self.emp.api_put_employee(username)
        print("修改员工响应结果为:",r.json())
        # 断言
        assert_common(self, r)

    # 查询员工
    def test03_get(self):
        # 调用查询接口
        r = self.emp.api_get_employee()
        print("查询员工响应结果为: ",r.json())
        # 断言
        assert_common(self,r)



    def test04_delete(self):
        # 调用删除员工方法
        r = self.emp.api_delete_employee()
        print("删除员工响应结果为:",r.json())
        # 断言
        assert_common(self,r)