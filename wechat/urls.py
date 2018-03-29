from django.urls import path
from . import views

app_name = 'wechat'
urlpatterns = [
    # 基于类视图的url
    path('', views.weixin_main, name='weixin_main'),

    ]