
from django.urls import path
from . import views

urlpatterns = [
    # ex: ex.com/
    path('', views.index, name='index'),
    # ex: ex.com/slug
    path('<slug:slug>', views.category_view, name='category_view'),
    path('products/<slug:slug>', views.products_view, name='products_view'),
    path('product/<slug:product_slug>', views.product_overview, name='product_overview'),
    # comment n rate
    path('rate/<slug:product_slug>', views.commentNrate, name="commentNrate"),
    path('user/sign', views.mySign, name="usersign"),
    # login register view
    path('user/signin', views.enterAccount, name="signin"),
    path('user/register', views.myRegister, name="register"),
    path('user/logout', views.myLogout, name="logout"),
    # settings n chats
    path('user/settings', views.mySettings, name="settings"),
    path('user/goods', views.myGoods, name="goods"),
    # upload good form 
    path('user/goods/upload', views.ImageFieldFormView.as_view(), name="uploadfile"),
    # bids
    path('user/bids', views.myBidsView, name="bids"),
    path('user/createbid', views.addBid, name="createbid"),
    # notifications
    path('user/notifications', views.myNotifications , name="notifications"),
    # chat view 
    path('user/mychats', views.chatView, name="chatview"),
    path('user/mychats/<str:username>', views.chatUser, name="chatuser"),
    path('user/mychats/addmsg/<str:username>', views.addMsg, name="addmsg"),
    # Contact button
    path('conctact/<str:username>', views.contactButton, name="contact"),

    # API 
    path('api/search', views.productSearch, name="search"),
    path('api/choosecategory', views.chooseCategory, name="choosecategory"),
    path('api/choosesubcategory', views.chooseSubCategory, name="choosesubcategory"),

    # Profile
    path('profile/<str:username>', views.profile, name="profile"),
]