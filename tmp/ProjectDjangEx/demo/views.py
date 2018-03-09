# coding:utf-8
'''
视图
'''
from django.http import HttpResponse
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from demo.models import Article,Comment

def helloWorld(request):
    return HttpResponse('Hello world!')

def havePar(request,uid):
    return HttpResponse('uid:%s' % uid)

def temTest(request):
    from django.template import Context, Template
    t = Template('My name is {{ name }}')
    c = Context({'name': 'Gregory'})
    t.render(c)

def index(request):
    import datetime
    s = 'hello'
    l = {111, 222, 333}  # 列表
    dic = {'name': 'yuan', 'age': 18}  # 字典
    date = datetime.date(1993, 5, 2)  # 日期对象

    class Person(object):
        def __init__(self,name):
            self.name = name
    person_yuan = Person('yuan')
    person_egon = Person('egon')
    person_alex = Person('alex')
    person_list = [person_yuan, person_egon, person_alex]
    return render_to_response('index.html', {'s': s, 'l': l, 'dic': dic, 'date': date, 'person_list': person_list})


def list(request):
    articles = Article.objects.order_by('id').all
    return render_to_response('list.html',{'articles':articles})

def add(request):
    if request.method == 'POST':
        content = request.POST.get('content',None)
        title = request.POST.get('title',None)
        new = Article(content=content,title=title)
        new.save()
        return HttpResponseRedirect('/list')

    return render_to_response('add.html',{'method_str':request.method})

def addComment(request):
    if request.method == 'POST':
        detail = request.POST.get('detail','')
        article_id = request.POST.get('article_id','')
        comment = Comment(Article=Article(id=article_id),detail=detail)
        comment.save()
        return HttpResponseRedirect('/view/%s' % article_id)

def findById(request,id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(Article=id).order_by('id').all()
    return render_to_response('view.html',{'article':article,'comments':comments})