# 导包
import unittest

from coonfig import BASE_DIR
from tools.HTMLTestReportCN import HTMLTestRunner

# 创建测试套件
# suite = unittest.TestLoader().discover(start_dir="./scripts")
suite = unittest.defaultTestLoader.discover(start_dir="./scripts")

# 获取报告存储的文件流 实例化HTMLTestRunner对象 调用run方法
with open(BASE_DIR + "/report/report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suite)
