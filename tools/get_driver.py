from selenium import webdriver
import page

class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 创建webdriver.Chrome的实例
            cls.driver = webdriver.Chrome()
            # 调用实例方法最大化窗口
            cls.driver.maximize_window()
            # 调用实例方法获取页面
            cls.driver.get(page.url)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        # 检查driver是否已经被设置为一个实例，并且不是None
        if cls.driver is not None:
            # 调用实例方法退出驱动
            cls.driver.quit()
            # 将driver设置为None
            cls.driver = None