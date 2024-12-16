import time
import unittest
from tools.get_driver import GetDriver
from page.cart import CartPage
from page.login import PageLogin


class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.cart = CartPage(cls.driver)#实例化driver
        cls.login = PageLogin(cls.driver)
        cls.login.page_click_login()  # 点击登录链接
        cls.login.page_login_success()
        cls.cart.page_back_to_index()

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()


    '''购物车测试用例'''
    def test_cart(self):
        try:

            self.cart.page_search_goods()#输入华为
            self.cart.page_search_btn()#点击搜索
            self.cart.page_add_to_cart()
            self.cart.page_cart_add_btn()
            time.sleep(2)
            #截图
            self.cart.page_cart_result_get_image()
            add_result = self.cart.page_cart_add_result()
            self.assertEqual('添加成功', add_result)
            #退出提示框
            self.cart.page_close_iframe()



        except Exception as e:
            print("测试失败:{}".format(e))

