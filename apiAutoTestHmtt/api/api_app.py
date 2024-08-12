from apiAutoTestHmtt import api
import requests
from apiAutoTestHmtt.tool.get_log import GetLog
log = GetLog.get_logger()
class ApiApp:
    # 初始化
    def __init__(self):
        # 1.登录url
        self.url_login = api.host + "/app/vl_0/authorizations"
        # 2.查询ur1
        self.url_article = api.host + "/app/v1_1/articles"
    # 登录
    def api_app_login(self, mobile, code):
        # 1.请求参数
        data = {"mobile": mobile, "code": code}
        # 2.调用post方法
        return requests.post(url=self.url_login, json = data, headers = api.headers)

    # 查询频道下所有文章
    def api_app_article(self):
        # 1.请求参数
        data = {"channel id": api.channel_id, "timestamp":int(time.time()), "with top": 1}
        # 2.调用get方法
        return requests.get(url=self.url_article, params = data, headers = api.headers)