import time
import unittest
from tools.get_driver import GetDriver
from tools.log_record import get_logger
from page.cart_order_submit import CartOrderSubmit
from page.login import PageLogin
from page.cart import CartPage
logger = get_logger(__name__)


class CartOrderSubmitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver.get_driver()
        cls.cart_order = CartOrderSubmit(cls.driver)#实例化driver对像
        cls.login = PageLogin(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.login.page_click_login()
        cls.login.page_login_success()
        cls.cart.page_back_to_index()

    @classmethod
    def tearDownClass(cls) :
        GetDriver.quit_driver()


    #测试用例
    def test_submit_cart_order(self):
        try:
            self.cart_order.page_cart_click()
            self.cart_order.page_cart_all_select()
            time.sleep(2)
            self.cart_order.page_go_to_pay()
            time.sleep(5)
            self.cart_order.page_submit_order()
            time.sleep(2)
            self.cart_order.page_get_ima()
            logger.info("[CartOrderSubmitTest]:正在进行断言")
            result = self.cart_order.page_submit_result()
            self.assertEqual('订单提交成功，请您尽快付款！', result)

        except Exception as e:
            logger.error(e)





