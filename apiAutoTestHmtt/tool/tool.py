from apiAutoTestHmtt.tool.get_log import GetLog
log = GetLog.get_logger()
import api

class Tool:
    #提取token
    @classmethod
    def commpn_token(cls, response):
        # 提取token
        token = response.json().get("data").get("token")
        # 追加请求信息头
        api.headers['Authorization'] = "Bearer" + token
        log.info("正在提取token：{}".format(api.headers))
        print("添加token后的headers为：", api.headers)
    #断言
    @classmethod
    def common_assert(cls, response, status_code=201):
        log.info("正在调用公共断言方法")
        # 断言状态码
        assert status_code == response.status_code
        # 断言响应信息
        assert "OK" == response.json().get("message")