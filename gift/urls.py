from django.conf.urls import url
from .import views

app_name='gift'
# gift子路由
urlpatterns = [

    # gift首页
    url(r'^$',views.gifts,name='gift'),

    #  首页礼物区域，page代表[加载更多]
    url(r'indexgifts/(?P<page>\d*)', views.Indexgifts, name='gifts'),

    # 礼物多条件查询
    url(r'getSelectGifts/(?P<dayid>\d+),(?P<objid>\d+),(?P<sortid>\d+),(?P<con>\w*),(?P<pindex>\d+)/',views.getSelectGifts,
        name='getSelectGifts'),

    # 多条件查询获取总页数
    url(r'getAllPages/(?P<dayid>\d+),(?P<objid>\d+),(?P<sortid>\d+),(?P<con>\w*),(?P<pindex>\d+)/',views.getAllPages,
        name='getAllPages'),

    # gift详情页
    url(r'getgift/(?P<giftid>\d+)/',views.getGiftDetail,name='getgift'),

    # gift详情页 评论
    url(r'giftcomments/(?P<giftid>\d+),(?P<cindex>\d+)/',views.getGiftsComments,name='giftcomments'),

    # 加入购物车
    url(r'addcart/',views.addCart,name='addcart'),

    # 获取购物车信息
    url(r'getallcarts/',views.getAllCarts,name='getallcarts'),

    # 删除商品
    url(r'delgift/', views.delSelectedGift, name='delgift'),

    # 清空购物车
    url(r'clearcart/', views.clearCart, name='clearcart'),

    # 订单展示
    url(r'showorder/(?P<userid>\d+),(?P<ordertype>[a-z]+),(?P<page>\d+)/', views.showOrder, name='showorder'),

    # 订单总页数
    url(r'getorderpage/(?P<userid>\d+),(?P<ordertype>[a-z]+)/', views.getOrderpage, name='getorderpage'),

    # 加入收藏夹
    url(r'addcollect/',views.addCollectGift,name='addcollect'),





    # 结算
    url(r'account/', views.account, name='account'),


    # 礼物类型
    url(r'type/',views.type,name='type'),

    # 攻略展示页面加载热门商品
    url(r'hotgoods/',views.gethotgo,name='gethotgo'),





]
