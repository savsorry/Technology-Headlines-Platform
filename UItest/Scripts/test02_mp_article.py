from tools.get_driver import GetDriver
import page



class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = Getdriver.get_web_driver(page.url_mp)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 获取pagempLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        # 获取pageamarticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()
    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()
    # 测试发布文章方法
    def test_mp_article(self):
        # 调用发布文章业务方法
        self.article.page_mp_article(title, content)
        # 查看断言信息
        print("发布文章结果为：", self.article.page_get_info())