import requests
from apiAutoTestHmtt import api

class ApiMis:
    def __init__(self):
        # 1.登录ur1
        self.url_login = api.host + "/mis/v1 0/authorizations"
        # 2.查询文章ur1
        self.url_search = api.host + "/mis/v1 0/articles"
        # 3.审核文章ur1
        self.url_audit = api.host + "/mis/v1 0/articles"

    # 2.登录
    def api_mis_login(self, account, password):
        # 参数数据
        data = {"account": account,"password": password}
        # 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 3.查询文章
    def api_mis_search(self):
        # 参数数据
        data = {"title": api.title, "channel": api.channel}
        # 调用get方法
        return requests.get(url=self.url_search, params=data, headers=api.headers)

    # 4.审核文章
    def api_mis_audit(self):
        # 参数数据
        data = {"article_ids": [api.article_id], "status": 2}
        # 调用put方法
        return requests.put(url=self.url_audit, json=data, headers=api.headers)