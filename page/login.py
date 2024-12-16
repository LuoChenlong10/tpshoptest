# 获取 浏览器驱动对象
import time

import page
from base.base import Base
from tools.get_driver import GetDriver

from tools.log_record import get_logger

logger = get_logger(__name__)#获取日志器
driver = GetDriver().get_driver()
class PageLogin(Base):
    # 页面操作，点击登录链接
    def page_click_login(self):
        logger.info('[PageLogin]:正在点击{}登录'.format(page.login_link))
        self.base_click(page.login_link)

    #页面操作，输入用户名
    def page_input_username(self,username):
        logger.info('[PageLogin]:正在对元素：{}输入用户名：{}'.format(page.login_username,username))
        self.base_input(page.login_username,username)

    #登录页面，输入密码
    def page_input_password(self,password):
        logger.info('[PageLogin]:正在对元素：{}输入密码：{}'.format(page.login_password,password))
        self.base_input(page.login_password,password)

    #登录页面，输入验正码
    def page_input_verifycode(self,verify_code):
        logger.info('[PageLogin]:正在对元素：{}输入验证码：{}'.format(page.login_verify_code,verify_code))
        self.base_input(page.login_verify_code,verify_code)

    #登录页面，点击登录
    def page_click_login_button(self):
        logger.info('[PageLogin]:正在对元素：{}进行点击'.format(page.login_btn))
        self.base_click(page.login_btn)

    #登录页面，当输入错误的信息登录时，获取错误提示信息
    def page_get_error_text(self):
        return self.base_get_text(page.login_err_info)

    #登录页面，点击错误提示信息的确定按钮
    def page_error_text_sure(self):
        logger.info('[PageLogin]:正在对元素{}进行确认操作'.format(page.login_err_btn_ok))
        self.base_click(page.login_err_btn_ok)

    #判断是否登录成功，点击登录之后，进入主页并且有‘安全退出’，那就登录成功
    def page_login_success_or_not(self):
        return self.base_element_exist_or_not(page.login_logout_btn)#存在就返回true

    #如果登录成功之后，点击安全退出
    def page_safe_logout(self):
        self.base_click(page.login_logout_btn)

    #判断是否退出，如果有登录链接这个元素存在，则退出成功
    def page_logout_success_or_not(self):
        return self.base_element_exist_or_not(page.login_link)


    #截图
    def page_login_get_img(self):

        self.driver.get_screenshot_as_file('../images/login-test-case/{}.png'.format(time.strftime("%Y-%m-%d %H-%M-%S")))

    #组合业务方法，登录业务直接调用
    def page_login(self,username,password,verify_code):
        logger.info('[PageLogin]:正在进行登录操作，用户名：{}，密码：{}，验证码：{}'.format(username,password,verify_code))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verifycode(verify_code)
        self.page_click_login_button()

    #组合登陆业务方法，给其他模块依赖登录使用
    def page_login_success(self,username='13100000000',password='123456',verify_code='8888'):
        logger.info('[PageLogin]:正在执行登录操作，用户名：{}，密码：{}，验证码：{}'.format(username,password,verify_code))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verifycode(verify_code)
        self.page_click_login_button()

