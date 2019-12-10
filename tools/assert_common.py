def assert_common(self,response,status_code=200,msg="操作成功！"):
    '''
    :param self: unittest.TestCase实例对象
    :param response: 接口请求后的响应对象
    :param status_code:默认状态码
    :param msg:默认消息
    '''
    # 断言响应状态码
    self.assertEqual(status_code,response.status_code)
    # 断言 code
    self.assertEqual(10000,response.json().get("code"))
    # 断言 success
    self.assertTrue(response.json().get("success"))
    # 断言 message
    self.assertEqual(msg,response.json().get("message"))