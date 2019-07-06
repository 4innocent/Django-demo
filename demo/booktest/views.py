from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 1.定义视图函数处理url请求
# 2.在项目的urls中引入app的urls，并配置正则项
# http://127.0.0.1:8080/index ----对应的即为index函数

# 必须传入HTTP请求
def index(request,e):
    # 返回一个django的HttpResponse，第一个参数为内容
    # return HttpResponse("我是返回的数据")

    # 定义模板需要使用的变量
    grams = {
        "content": "这是变量渲染出来的文字",
        "list": list(range(0,9)),
    }

    # 使用render函数替换模板中的变量,第一个变量是请求，第二个是模板的地址，第三个是数据
    return render(request,"booktest/index.html",grams)
