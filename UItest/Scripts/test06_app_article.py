from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
log = GetLog.get_logger()
from tools.read_yaml import read_yaml


class TestAppArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 调用登录方法
        self.page_in.page_get_PageAppLogin().page_app_login_success()
        # 获取发布文章页面对象
        self.article = self.page_in.page_get_PageMpArticle()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()
    # 发布文章测试方法
    @pytext.mark.parametrize("click_text,title", read_yaml("app_article.yaml"))
    def test_app_article(self, click_text="python", title="Python"):
        try:
            # 调用发布文章业务方法
            self.article.page_app_article(click_text, title)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.audit.base_get_img()
            # 抛异常
            raise
