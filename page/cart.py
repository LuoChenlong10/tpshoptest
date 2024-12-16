import time

import page
from base.base import Base
from tools.log_record import get_logger
from tools.get_driver import GetDriver

driver = GetDriver().get_driver()
logger = get_logger(__name__)
class CartPage(Base):

    '''打开首页'''
    def page_back_to_index(self):
        #先暂停2s，否则url会出现问题
        time.sleep(2)
        logger.info("[CartPage]:正在打开首页 ")
        self.base_back_to_index()


    '''在输入框输入华为'''
    def page_search_goods(self,value="华为"):
        logger.info("[CartPage]:正在输入值：{}".format(value))
        self.base_input(page.search_input_box,value)

    '''点击搜索按钮'''
    def page_search_btn(self):
        logger.info("[CartPage]:正在点击搜索按钮")
        self.base_click(page.search_btn)

    '''点击加入购物车进入详情页'''
    def page_add_to_cart(self):
        logger.info("[CartPage]:正在点击加入购物车")
        self.base_click(page.add_to_cart)

    '''点击加入购物车，添加商品'''
    def page_cart_add_btn(self):
        logger.info("[CartPage]:正在点击加入购物车，添加商品")
        self.base_click(page.add_to_cart_btn)

    '''获取添加结果'''
    def page_cart_add_result(self):
        logger.info("[CartPage]:正在切换iframe")
        self.base_iframe_switch(page.cart_add_after_iframe)#切换iframe
        logger.info("[CartPage]:正在获取添加结果")
        add_result = self.base_get_text(page.cart_add_result)
        return add_result

    '''退出提示框'''
    def page_close_iframe(self):
        logger.info("[CartPage]:回到默认目录")
        self.base_default_content()
        logger.info("[CartPage]:正在点击退出提示框")
        self.base_click(page.cart_windows_close)

    '''添加结果截图'''
    def page_cart_result_get_image(self):
        driver.get_screenshot_as_file("../images/cart-test-case/{}.png".format(time.strftime("%Y-%m-%d %H-%M-%S")))


    '''购物车操作组合'''
    def page_cart(self):
        logger.info("[CartPage]:正在执行购物车操作")
        self.page_search_goods()
        self.page_search_btn()
        self.page_add_to_cart()
        self.page_cart_add_btn()


