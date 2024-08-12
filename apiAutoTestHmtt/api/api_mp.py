import api
import requests
from apiAutoTestHmtt.tool.get_log import GetLog
log = GetLog.get_logger()

class ApiMp:
    # 初始化
    def __init__(self):
        # 登录接口url
        self.url_login = "/mp/v1_0/authorizations"
        log.info("正在初始化自媒体登录url")
        # 发布文章接口url
        self.url_article = "/mp/v1_0/articles"
        log.info("正在初始化自媒体发布文章url：{}".format(self.url_article))

    # 登录接口
    def api_mp_login(self, r, mobile, code):
        # 定义请求数据
        #data = {"mobile": "13012345678", "code": "246810"}
        data = {"mobile": mobile, "code": code}
        log.info("正在调用自媒体登录接口，请求数据：{}".format(data))
        # 调用post方法
        return r.client.post(url=self.url_login, json=data, header=api.headers)

    # 发布文章接口
    def api_mp_article(self, r, title, content, channel_id):
        # 定义请求数据
        data = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type":0,"images":[]}}
        log.info("正在调用自媒体发布文章接口，请求数据：{}".format(data))
        # 调用post方法
        return r.client.post(url=self.url_article, json=data, headers=api.headers)