from django.conf.urls import url
from .import views

app_name='mydata'
# mydata子路由
urlpatterns = [

    url(r'^$',views.mydata,name='mydata'),

]
