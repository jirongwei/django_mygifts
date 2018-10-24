
from django.conf.urls import url
from .import views

app_name='post'
# user子路由
urlpatterns = [

    # personal首页
    url(r'^$',views.personal,name='post'),

    # 用户基本信息
    url(r'getuserinfo/', views.getUserInfo, name='getuserinfo'),

    # update用户信息
    url(r'updateinfo/', views.updateUserInfo, name='updateinfo'),

    # 上传头像
    url(r'uploadicon/', views.uploadIcon, name='uploadicon'),

    # 安全等级
    url(r'security/', views.securityLevel, name='security'),

    # 修改密码
    url(r'updatepwd/', views.updatePwd, name='updatepwd'),

    # 绑定手机
    url(r'bindphone/', views.bindPhone, name='bindphone'),

    # 收藏管理
    # 1.展示收藏
    url(r'collects/', views.getCollectList, name='collects'),

    # 2.详情信息
    url(r'getcollect/', views.getCollectDetail, name='getcollect'),

    # 3.删除收藏
    url(r'delcollect/', views.delCollect, name='delcollect'),

    # 订单管理
    url(r'orders/', views.getOrderList, name='orders'),

    # 订单详情
    url(r'getorder/', views.getOrderDetail, name='getorder'),

    # 地址管理
    url(r'addresses/', views.getAddressList, name='addresses'),

    # 添加地址
    url(r'add/', views.addAddress, name='add'),

    # 修改地址
    url(r'upaddr/', views.updateAddress, name='upaddr'),

    # 删除地址
    url(r'deladdr/', views.delAddress, name='deladdr'),

    # 插入帖子
    url(r'createPost/', views.createPost, name='createPost'),

    #加载帖子（根据类型，页码）Post
    url(r'showpost/', views.showPost, name='showPost'),

    #收藏帖子
    url(r'collectpost/', views.collectpost, name='collectpost'),

    #点赞帖子
    url(r'dianzanpost/', views.dianzanpost, name='dianzanpost'),
]
