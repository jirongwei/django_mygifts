
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

    # 根据token获取用户基本信息
    url(r'^userinfo\w*/',views.getUserInfo,name='userinfo'),

    # 修改用户基本信息
    url(r'^updatemsg\w*/',views.updateMsg,name='updatemsg'),

    # 修改密码
    url(r'^updatepwd\w*/',views.updatePassword,name='updatepwd'),

    # 绑定手机号
    url(r'^bindphone\w*/',views.bindPhone,name='bindMsg'),

    # 获取用户所有地址
    url(r'^getaddress\w*/',views.getAllAddress,name='getaddress'),

    # 添加地址
    url(r'^addaddr\w*/',views.addAddr,name='addaddr'),

    # 获取修改地址信息
    url(r'^getupdate\w*/(?P<addrid>\d+)',views.updateAddr,name='getupdate'),

    # 修改地址
    url(r'^updateaddress\w*/(?P<addrid>\d+)',views.updateAddress,name='updateaddress'),

    # 删除地址
    url(r'^deladdr\w*/(?P<addrid>\d+)',views.delAddr,name='deladdr'),

    # 用户头像上传，通过图片名称，返回七牛token和图片名称
    url(r'qiniutoken/',views.sendToken, name='sendToken'),

    # 给你一个图片名，将图片名存到头像表中，并且把当前用户的头像id改为新头像id
    url(r'^iconurl\w*/(?P<url>.*)/',views.getIconUrl,name='iconurl'),

    # 获取当前用户头像
    url(r'^usericon\w*/',views.getUserIcon,name='usericon'),

    # 获取当前登录用户的头像，昵称，积分
    url(r'^getloginuser\w*/',views.getLoginUser,name='getloginuser'),


    # 根据token查询一定的用户信息 postRight
    url(r'gettoken', views.getUserbyToken, name='getUserbyToken'),

    # 根据userid查询用户收货地址
    url(r'getaddr', views.getaddr, name='getaddr'),

]
