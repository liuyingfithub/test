# coding:utf-8
"""ProjectDjangEx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

url(regex,view,kwargs,name)：可以接收4个参数，前2个为必选参数，后2个为可选参数
1）、regex：正则表达式，与之匹配的URL会执行对应的第二个参数view
2）、view：用于执行与正则表达式匹配的URL请求；
3）、kwargs：视图使用的字典典型的参数
4）、name：用来反向获取URL
"""
from django.conf.urls import url
from django.contrib import admin

from demo import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^helloWorld$', views.helloWorld),
    url(r'^havePar_(?P<uid>[\d]+)$', views.havePar),  # 特殊分组法：分组，除了原有的编号外再指定一个额外的别名
    url(r'^tempTest$', views.temTest),
    url(r'^index$', views.index),
    url(r'^add$', views.add),
    url(r'^list$', views.list),
    url(r'^view/(?P<id>[\d]+)$', views.findById),
    url(r'^add/comment', views.addComment)
]
