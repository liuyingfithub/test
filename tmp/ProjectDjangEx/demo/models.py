# coding:utf-8
'''
model：发布文章的基本对象
'''
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

class Comment(models.Model):
    Article = models.ForeignKey(Article, related_name='article_comment')
    detail = models.TextField()