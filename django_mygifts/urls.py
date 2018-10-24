"""django_mygifts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# 配置路由的两种机制
# from django.urls import path,include
from django.conf.urls import url,include

from .import views



urlpatterns = [
    url('admin/', admin.site.urls),


    # 匹配空路由
    url(r'^$', views.index, name='myindex'),



    # 轮播图展示
    url(r'sowingmap/', views.som, name='som'),

    # 模块子路由部分
    url(r'^user/',include('user.urls',namespace='django_mygifts.user')),
    url(r'^post/',include('post.urls',namespace='django_mygifts.post')),
    url(r'^gift/',include('gift.urls',namespace='django_mygifts.gift')),
    url(r'^tribune/',include('tribune.urls',namespace='django_mygifts.tribune')),
    url(r'^vein/',include('vein.urls',namespace='django_mygifts.vein')),

    # 数据处理子路由
    url(r'^mydata/',include('mydata.urls', namespace='django_mygifts.mydata')),
]
