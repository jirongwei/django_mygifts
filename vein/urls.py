from django.conf.urls import url
from .import views

app_name='vein'
# vein子路由
urlpatterns = [

    # vein首页
    url(r'^$',views.vein,name='vein'),

    # 查看基本信息
    url(r'getinfo/', views.getBasicInfo, name='getinfo'),

    # 私信
    url(r'private/', views.privateLetter, name='private'),



]

