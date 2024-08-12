from base.app_base import AppBase
import page
from tools.get_log import GetLog
log = GetLog.get_logger()

class PageAppArticle(AppBase):
    # 查找频道
    def page_click_channel(self, click_text):
        # 调用 从右向左滑动方法
        self.app_base_right_wipe_left(page.app_channel_area, click_text)

    # 查找文章
    def page_click_article(self):
        # 调用 从下向上滑动的方法
        self.app_base_down_wipe_up(page.app_article_area, click_text-title)
    # 查找文章业务方法
    def page_app_article(self, find_text, title):
        log.info("正在调用查找文章业务方法 所属频道：{} 文章标题：{}".format(find_text, title))
        # 调用查找频道
        self.page_click_channel(find_text)
        # 调用查找文章
        self.page_click_article(title)

