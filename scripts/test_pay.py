import time
from unittest import TestCase
from tools.get_driver import GetDriver
from tools.log_record import get_logger
from page.order_to_pay import OrderToPay
from page.login import PageLogin
from page.cart import CartPage

logger = get_logger(__name__)
driver = GetDriver()


class PayTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.pay = OrderToPay(cls.driver)
        cls.login = PageLogin(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.login.page_click_login()
        cls.login.page_login_success()
        cls.cart.page_back_to_index()

    @classmethod
    def tearDownClass(cls):
        driver.quit_driver()

    '''测试用例'''
    def test_pay(self):
        try:
            self.pay.page_pay_order_link()
            self.pay.page_pay_now()
            self.pay.page_pay_way()
            self.pay.page_confirm_pay()
            time.sleep(2)
            self.pay.page_get_image()
            #获取支付结果
            pay_result = self.pay.page_get_pay_result()
            #设置断言
            self.assertEqual('订单提交成功，我们将在第一时间给你发货！', pay_result)


        except Exception as e:
            logger.error(e)







