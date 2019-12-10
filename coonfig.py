import os




"""
os.path.abspath(__file__) --> 获取当前文件绝对路径
os.path.dirname() --> 截取目录部分,获得的刚好是项目目录
"""
# 将项目路径保存给一个变量 --> 外面使用导包使用
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
# print(os.path.abspath(__file__))