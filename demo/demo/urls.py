"""demo URL Configuration

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
from django.urls import path,include
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 包含app的urls，在路由查找是第一步先从项目urls查找如果有匹配在匹配项中查找
    # 如果booktest/index匹配项为 r"^booktest/",那么在进行第二次匹配时会删除第一次匹配到的字符串，即为index
    url(r'^',include("booktest.urls"))
]
