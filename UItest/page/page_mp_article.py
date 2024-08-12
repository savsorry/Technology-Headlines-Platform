from base.web_base import WebBase
import page
class PageMpArticle(WebBase):
    # 点击 内容管理
    def page_click_content_manage(self):
        self.base_click(page.mp_content_manage)
    # 点击 发布文章
    def page_click_publish_article(self):
        self.base_click(page.mp_publish_article)
    # 输入标题
    def page_input_title(self, title):
        self.base_input(page.mp_title, title)
    # 输入内容
    def page_input_content(self):
        #切换iframe
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        #输入内容
        self.base_input(page.mp_content,content)
        #回到默认目录
        self.driver.switch_to.default_content()
    # 选择封面
    def page_click_cover(self):
        self.base_click(page.mp_cover)
    # 选择频道
    def page_click_channel(self):
        # 调用webBase封装方法
        self.web_base_click_element(placeholder_text="请选择", click_text=page.channel)
    # 点击 发表按钮
    def page_click_submit(self):
        self.base_click(page.mp_submit)
    # 获取 发表提示信息
    def page_get_info(self):
    # 组合发布文章业务方法
    def page_mp_article(self, title, content):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()
