from selenium import webdriver
from appium import webdriver
import page

class GetDriver:
    # 声名变量
    __web_driver = None
    # 声明app中driver变量
    __app_driver = None

    # 获取driver方法
    @classmethod
    def get_web_driver(cls):
        # 判断是空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 滞空操作 重点
            cls.__web_driver = None
    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断__app_driver为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '5.1'
            # 必填
            desired_caps['deviceName'] = '192.168.56.101:5555'
            # APP包名
            desired_caps['appPackage'] = page.appPackage
            # 启动名
            desired_caps['appActivity'] = page.appActivity
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wb/hub", desired_caps)
        # 返回cls. app_driver
        return cls.__app_driver

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 滞空操作 重点
            cls.__app_driver = None
