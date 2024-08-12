from base.base import Base

class WebBase(Base):
    """
    web项目专属方法
    """
    #根据显示文本点击指定元素
    def web_base_click_element(self, placeholder_text, click_text):
        log.info("正在调用web专属点击封装方法")
        #点击复选框
        loc = By.CSS_SELECTOR, "[placeholder = '{}']".format(placeholder_text)
        self.base_click(loc)
        # 暂停
        sleep(1)
        #点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

     #判断页面是否包含指定元素
    def web_base_is_exist(self, text):
        log.info("正在调用查找页面是否包含指定元素：{}方法".format(text))
        # 组装元素配置信息
        loc = By.XPATH, "//*[text()='{}']".format(text)
        # 找元素
        try:
            # 找元素，修改找元素时间
            self.base_find(loc, timeout=3)
            # 输出找到的信息
            print("找到：{}元素啦！".format(loc))
            # 返回true
            return True
        except:
            # 输出未找到信息
            print("没有找到：{}信息".format(loc))
            # 返回false
            return False