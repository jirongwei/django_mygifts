
from django.conf.urls import url
from .import views

app_name='user'
# user子路由
urlpatterns = [

    # user首页
    url(r'^$',views.index,name='index'),

    # 用户登录
    url('login/', views.login, name='login'),

    # 用户注册
    url('regist/', views.regist, name='regist'),

    # 根据id判断用户是否存在
    url(r'^getuser\w*/(?P<id>\d*)', views.getUserById, name='getuser'),

    # 获取短信验证接口
    url(r'^sendmessage\w*/(?P<user_telephone>\d*)',views.sendMessage,name='sendmessage'),

    # 根据token查询一定的用户信息 postRight
    url(r'gettoken', views.getUserbyToken, name='getUserbyToken'),



]
