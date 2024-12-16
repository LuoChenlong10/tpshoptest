from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import page
from tools.log_record import get_logger

logger = get_logger(__name__)



class Base:
    def __init__(self,driver):
        logger.info("[base:]正在获取初始化driver对象：{}".format(driver))
        self.driver = driver

    '''查找元素的方法'''

    def base_find_element(self, locator, timeout=10, poll=0.5):
        try:
            print(f"尝试寻找元素: {locator}")
            element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"在寻找元素的时候超时了: {locator}")
            raise


    '''输入元素方法'''
    def base_input(self,locator,value):
        logger.info("[base]:正在获取元素：{}".format(locator))
        ele = self.base_find_element(locator)#获取元素
        logger.info("[base]:正在对元素：{}进行清空".format(locator))
        ele.clear()#清空输入框
        logger.info("[base]:正在给{}元素输入内容：{}".format(locator,value))
        ele.send_keys(value)#输入值

    '''点击元素方法'''
    def base_click(self,locator):
        logger.info("[base]:正在点击元素：{}".format(locator))
        self.base_find_element(locator).click()

    '''获取文本信息（弹出窗）'''
    def base_get_text(self,locator):
        logger.info("[base]:正在获取文本值：{}".format(locator))
        return self.base_find_element(locator).text

    '''截图方法'''
    # def base_get_image(self):
    #     self.driver.get_screenshot_as_file("../images/{}.png".format(time.strftime("%Y-%m-%d %H-%M-%S")))

    '''判断元素是否存在'''
    def base_element_exist_or_not(self,locator):
        try:
            self.base_find_element(locator,timeout=2)
            logger.info("[base]:{}元素查找成功".format(locator))
            return True

        except:
            logger.info("[base]:{}元素查找失败".format(locator))
            return False

    '''返回主页'''
    def base_back_to_index(self):
        logger.info("[base]:正在返回主页")
        self.driver.get(page.url)


    '''切换iframe'''
    def base_iframe_switch(self,element):
        logger.info("[base]:正在切换iframe表单")
        self.driver.switch_to.frame(element)

    '''回到默认目录'''
    def base_default_content(self):
        logger.info("[base]:正在回到默认目录")
        self.driver.switch_to.default_content()

    '''切换窗口'''
    def base_switch_window(self,title):
        logger.info("[base]:正在切换窗口{}".format(title))
        self.base_get_title_handel(title)#切换到当前标题页句柄的页面

    '''获取指定title页面的句柄'''
    def base_get_title_handel(self,title):
        handles = self.driver.window_handles#获取当前所有句柄
        for handle in handles:#遍历所有句柄
            logger.info("[base]:正在遍历所有句柄：{}->{}".format(handle,handles))
            self.driver.switch_to.window(handle)#切换句柄
            logger.info("[base]:切换窗口：{}".format(handle))
            #获取当前页面的title，判断是否等于指定的title，如果是就返回该句柄
            if self.driver.title == title:
                return handle


