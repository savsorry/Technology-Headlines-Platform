from base.base import Base
from tools.get_log import GetLog
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
log = GetLog.get_logger()
from time import sleep
class AppBase(Base):
    # 查找页面是否存在指定元素
    def app_base_is_exist(self, loc):
        try:
            # 调用查找方法
            self.base_find(loc, timeout=3)
            log.info("在app页面中找到指定元素！")
            # 输出信息
            print("找到：{}元素啦".format(loc))
            # 返回true
            return True
        except:
            log.error("没有在app页面中找到指定元素！")
            # 输出信息
            print(" 未找到：{}元素".format(loc))
            # 返回false
            return False
    #从右向左滑动屏幕
    def app_base_right_wipe_left(self, loc_area, click_text):
        log.info("正在调用 从下向上滑动方法")
        # 查找区域元素
        el = self.base_find(loc_area)
        # 获取区域元素的位置 y坐标点
        y = el.location("y")
        # 获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height *0.5

        #组合频道元素配置信息
        loc = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']//*[contains(@text,'{}')]".format(click_text)
        # 循环操作
        while True:
            # 1.获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2.捕获异常
            try:
                sleep(2)
                # 查找元素
                el = self.base_find(loc, timeout=2)
                # 输出提示信息
                print("找到{}元素啦".format(loc))
                sleep(2)
                # 点击元素
                el.click()
                # 跳出循环
                break
            # 3.处理异常
            except:
                # 输出提示信息
                print("未找到：{}元素！".format(loc))
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)

            # 4.判断是否为最后一页
            if page_source == self.driver.page_source:
                # 输出提示信息
                print("划到屏幕最后，未找到元素！")
                # 抛出未找到元素异常
                raise NoSuchElementException
    # 从下向上滑动屏幕
    def app_base_down_wipe_up(self, loc_area, click_text):
        log.info("正在调用 从下向上滑动方法")
        # 查找区域元素
        el = self.base_find(loc_area)
        # 获取区域元素的位置 y坐标点
        y = el.location("y")
        # 获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算
        start_x = width * 0.5
        start_y = y + height * 0.8
        end_x = width * 0.5
        end_y = y + height *0.2

        #组合频道元素配置信息
        loc = By.XPATH, "//*[@bounds='[0,520][1440,2288]']/*[contains(@text,'{}')]".format(click_text)
        # 循环操作
        while True:
            # 1.获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2.捕获异常
            try:
                # 查找元素
                el = self.base_find(loc, timeout=2)
                # 输出提示信息
                print("找到{}元素啦".format(loc))
                # 点击元素
                el.click()
                # 跳出循环
                break
            # 3.处理异常
            except:
                # 输出提示信息
                print("未找到：{}元素！".format(loc))
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)

            # 4.判断是否为最后一页
            if page_source == self.driver.page_source:
                # 输出提示信息
                print("划到屏幕最后，未找到元素！")
                # 抛出未找到元素异常
                raise NoSuchElementException