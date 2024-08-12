from apiAutoTestHmtt.api.api_app import ApiApp
from apiAutoTestHmtt.api.api_mis import ApiMis
from apiAutoTestHmtt.tool.tool import Tool
from apiAutoTestHmtt.tool.tool import read_yaml
from apiAutoTestHmtt.tool.get_log import GetLog
log = GetLog.get_logger()

import pytest

class TestApp:
    # 初始化
    def setup_class(self):
        # 获取ApiApp对象
        self.app = ApiApp()

    # 登录测试接口
    @pytest.mark.parametrize("mobile,code", read_yaml("mp_login.yaml"))
    def test01_app_login(self, mobile, code):
        # 调用登录接口
        r = self.app.api_app_login(mobile, code)
        # 提取token
        Tool.common_token(r)
        try:
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 查询频道下所有文章测试接口
    def test02_app_article(self):
        # 调用查询接口
        r = self.app.api_app_article()
        try:
            # 断言
            Tool.common_assert(r, status_code=200)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

