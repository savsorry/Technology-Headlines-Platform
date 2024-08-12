from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
log = GetLog.get_logger()



class TestAppLogin:
    # 1.初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_app_driver()
        # 2.通过统一入口对象获取PageappLogin对象
        self.login = PageIn(driver).page_get_PageAppLogin()

    # 2.结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 3.app登录测试业务方法
    @pytest.mark.parametrize("phone,code", read_yaml("app_login.yaml"))
    def test_app_login(self, phone="13812345678", code="246810"):
        # 调用app登录业务方法
        self.login.page_app_login(phone, code)
        # 调试断言
        try:
            # 断言
            assert self.login.page_is_login_success()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.audit.base_get_img()
            # 抛异常
            raise