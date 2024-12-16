# 导包
import unittest
import time

from page.login import PageLogin
from parameterized import parameterized
from tools.log_record import get_logger
from tools.get_driver import GetDriver
from tools.read_json import write_json


# 获取数据

logger = get_logger(__name__)

# 新建测试类并继承
class TestLongin(unittest.TestCase):

    # setupClass(只执行一次）
    @classmethod
    def setUpClass(cls) :
        try:
            cls.driver = GetDriver().get_driver()#实例化，获取driver
            cls.login = PageLogin(cls.driver)#实例化Page_login
            cls.login.page_click_login()#点击登录链接
        except Exception as e:

            print(e)

    @classmethod
    def tearDownClass(cls) :
        GetDriver.quit_driver()#关闭驱动

    '''测试方法'''
    @parameterized.expand(write_json())


    def test_login(self, username, password, verify_code, expect_result, status):
        try:
            # 调用 登录业务方法
            self.login.page_login(username, password, verify_code)

            # 判断是否为正向
            if status == "true":
                # 断言是否登录成功
                try:
                    time.sleep(2)
                    self.login.page_login_get_img()
                    self.assertTrue(self.login.page_login_success_or_not())
                except Exception as e:

                    # 日志
                    logger.error("登录成功但出现了其他错误：{}".format(e))
                # 点击 安全退出
                self.login.page_safe_logout()
                # 点击 登录链接
                self.login.page_click_login()
            # 逆向用例
            else:
                # 获取错误提示信息
                time.sleep(2)
                msg = self.login.page_get_error_text()
                self.login.page_login_get_img()
                print("msg:", msg)
                try:
                    self.assertEqual(msg, expect_result)
                except Exception as e:
                    # 日志
                    logger.error("登陆失败：{}".format(e))
                # 点击错误提示框 确定按钮
                self.login.page_error_text_sure()
        except Exception as e:
            logger.error("出错了：{}".format(e))





