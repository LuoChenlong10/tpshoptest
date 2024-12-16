import time
from base.base import Base
import page
from tools.log_record import get_logger
logger = get_logger(__name__)

class OrderToPay(Base):

    '''我的订单'''
    def page_pay_order_link(self):
        logger.info('[OrderToPay]:正在点击我的订单链接')
        self.base_click(page.my_order_link)

    '''立即支付'''
    def page_pay_now(self):
        logger.info('[page_pay_now]:正在切换窗口')
        self.base_switch_window(page.my_order_title)
        logger.info('[page_pay_now]:正在点击立即支付')
        self.base_click(page.to_pay_now)

    '''点击货到付款'''
    def page_pay_way(self):
        logger.info('[page_pay_way]:正在切换页面')
        self.base_switch_window(page.pay_title)
        logger.info('[page_pay_way]:正在点击货到付款')
        self.base_click(page.pay_way)

    '''确认支付'''
    def page_confirm_pay(self):
        logger.info('[page_confirm_pay]:正在点击确认支付')
        self.base_click(page.confirm_pay_way)

    '''获取支付结果'''
    def page_get_pay_result(self):
        logger.info('[page_get_pay_result]:正在获取支付结果')
        pay_result = self.base_get_text(page.pay_result)
        return pay_result

    '''截图'''
    def page_get_image(self):
        logger.info('[page_get_image]:正在截图')
        self.driver.get_screenshot_as_file('../images/pay_test_case/{}.png'.format(time.strftime('%Y-%m-%d %H-%M-%S')))

    '''组合支付业务'''
    def page_pay(self):
        logger.info('[page_pay]:正在对订单进行支付')
        self.page_pay_order_link()
        self.page_pay_now()
        self.page_pay_way()
        self.page_confirm_pay()

