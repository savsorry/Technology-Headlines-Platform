from apiAutoTestHmtt.api.api_mis import ApiMis
from apiAutoTestHmtt.tool.tool import Tool
from apiAutoTestHmtt.tool.tool import read_yaml
from apiAutoTestHmtt.tool.get_log import GetLog
log = GetLog.get_logger()
import api
import pytest


class TestMis:
    #1.初始化
    def setup_class(self):
        # 获取apimis对象
        self.mis =ApiMis()
    # 2.登录
    @pytest.mark.parametrize("account,password", read_yaml("mis_login.yaml"))
    def test01_mis_login(self,account,password):
        # 1.调用登录接口
        r = self.mis.api_mis_login(account,password)
        #2.提取token
        Tool.common_token(r)
        print("后台管理系统登录后，请求headers为:", api.headers)
        #3.断言
        try:
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 查询文章
    def test02_mis_search(self):
        # 调用查询文章接口
        r = self.mis.api_mis_search()
        try:
            # 断言
            Tool.common_assert(r, status_code=200)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise
    # 审核文章
    def test03_mis_audit(self):
        # 调用审核文章接口
        r = self.mis.api_mis_audit()
        try:
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise