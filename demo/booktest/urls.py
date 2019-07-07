from django.conf.urls import url
from booktest import views

# 在urlpatterns中添加路由匹配规则
urlpatterns = [
    # url的正则中()表达式中的内容会作为参数传入views的函数中
    url(r'^index(/?)$', views.index),
    url(r'^books/$', views.books_re),
    url(r'^books/(\d+)$', views.detail)
]