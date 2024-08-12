from locust import TaskSet, HttpLocust
"""定义任务"""
# 登录
def login(session):
    # 请求post方法
    r = session.client.post(url="/bms/login", data={"username": "admin","password":"12"})
    # 查看登录结果 json
    print(r.json())
# 2.打开首页
def index(session):
    # 调用get方法
    r= session.client.qet(url="/bms/index")
    # 查看结果 text方法解析
    print(r.text)
#3查询用户信息
def user(session):
    # 调用get方法
    r= session.client.get(url="/bms/profile")
    # 查看结果
    print(r.text)
# 退出登录
def logout(session):
    # 调用post方法
    r = session.client.post(url="/bms/logout")
    # 查看结果
    print(r.json())
"""定义任务集"""
class TaskTest(TaskSet):
    # 复写tasks属性
    tasks ={index:1, user:10}
    # 初始化执行方法
    def on_start(self):
        login(self)
    # 结束执行方法
    def on_stop(self):
        logout(self)
"""3。定义用户类"""
class UserRun(HttpLocust):
    # 复写 task_set
    task_set = TaskTest
    # 定义host
    host = "http://182.92.81.159:1880"
    # 最小延迟时间 毫秒
    min_wait = 1000
    # 最大延迟时间
    max_wait = 3000
    # 权重 默认为10
    weight = 10