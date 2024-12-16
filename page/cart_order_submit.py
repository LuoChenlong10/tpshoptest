import time

from base.base import Base

from tools.log_record import get_logger

import page

logger = get_logger(__name__)

class CartOrderSubmit(Base):

    '''点击主页我的购物车'''
    def page_cart_click(self):
        logger.info('[CartOrderSubmit]:正在点击我的购物车')
        self.base_click(page.cart_btn)

    '''点击全选'''
    def page_cart_all_select(self):
        logger.info('[CartOrderSubmit]:正在全选商品')
        self.base_click(page.select_all_btn)
    '''去结算'''
    def page_go_to_pay(self):
        logger.info('[CartOrderSubmit]:正在点击去结算')
        self.base_click(page.go_to_pay)

    '''提交订单'''
    def page_submit_order(self):
        logger.info('[CartOrderSubmit]:正在点击提交订单')
        self.base_click(page.order_submit_btn)

    '''获取提交结果'''
    def page_submit_result(self):
        logger.info('[CartOrderSubmit]:正在获取提交结果')
        sub_result = self.base_get_text(page.submit_result)
        return sub_result

    '''截图'''
    def page_get_ima(self):
        logger.info('[CartOrderSubmit]:正在对提交结果截图')
        self.driver.get_screenshot_as_file('../images/cart_order_test_case/{}.png'.format(time.strftime("%Y-%m-%d %H-%M-%S")))

    '''组合业务'''
    def page_cart_order(self):
        logger.info('[CartOrderSubmit]:正在执行购物车商品提交业务')
        self.page_cart_click()
        self.page_cart_all_select()
        self.page_go_to_pay()
        self.page_submit_order()


