from django.conf.urls import url
from .import views

app_name='tribune'
# tribune子路由
urlpatterns = [

    # tribune首页
    url(r'^$',views.tribunes,name='tribune'),

    # 首页攻略展示，page代表[加载更多]
    url(r'tribunes/(?P<page>\d*)', views.tribunes, name='tribunes'),


    # 攻略点赞
    url(r'thumbup/',views.thumbUpPost,name='thumbup'),

    # 攻略评论
    url(r'comment/',views.commentPost,name='comment'),

    # 发表攻略
    url(r'publish/',views.publishPost,name='publish'),

    # 收藏攻略
    url(r'collect/', views.collectStrategy, name='collect'),

    # 关注
    url(r'publisher/', views.concernPublisher, name='publisher'),

    # 热门攻略 Postright
    url(r'hottri/', views.hottribune, name='hottribune'),


]


