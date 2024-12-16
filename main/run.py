import time
import unittest
from tools.HTMLTestRunner import HTMLTestRunner

test_scripts = [
    "test_login",
    "test_cart",
    "test_cart_order_submit",
    "test_pay"
]
#创建测试套件
suite = unittest.TestSuite()

#按顺序加载测试用例
for script in test_scripts:
    try:
        #动态导入模块
        module = __import__(f"scripts.{script}",fromlist=[script])
        #使用unitest的defaultTestLoarder加载测试用例
        suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))
    except Exception as e:
        print(f"加载失败{script}:{e}")





filepath = "../reports/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))

with open(filepath,"wb") as f:
    HTMLTestRunner(f).run(suite)

