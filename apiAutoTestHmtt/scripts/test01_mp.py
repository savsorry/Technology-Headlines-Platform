import api
from apiAutoTestHmtt.tool.tool import Tool
from apiAutoTestHmtt.tool.get_log import GetLog
from apiAutoTestHmtt.tool.read_yaml import read_yaml
log = GetLog.get_logger()
from locust import TaskSet

class TestMp(TaskSet):
    # 初始化
    def setup_class(self):
        #获取ApiMp对象
        self.mp = api.ApiMp()
    # LOCUST中初始化方法
    def on_start(self):
        self.setup_class()

    # 登录接口测试方法
    #@pytest.mark.parametrize("mobile, code", read_yaml("mp_login.yaml"))
    @task
    def test01_mp_login(self, mobile="123456", code="4564321"):
        # 调用登录接口
        r = self.mp.api_mp_login(self, mobile, code)
        # 打印输出结果
        print("登录的结果为：", r.json())
        try:
            #提取token
            Tool.common_token(r)
            #断言
            Tool.common_assert(r)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise


    # 发布文章测试接口方法
    @task
    def test02_mp_article(self,title = api.title, content=api.content, channel_id=api.channel_id):
        # 调用发布文章接口
        r = self.mp.api_mp_article(self, title, content, channel_id)
        # 提取id
        api.article_id = r.json().get("data").get("id")
        # 断言
        try:
            Tool.common_assert(r)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise
class UserRun(HttpLocust):
    # task_set
    task_set = TestMp
    # host
    host = api.host