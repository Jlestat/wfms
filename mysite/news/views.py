from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.all()
    res = '<h1>Список новостей </h1>'
    for i in news:
        res += f'<div>\n<p>{i.title}</p>\n<p>{i.content}</p>\n</div><hr>\n'
    return HttpResponse(res)


def test(request):
    return HttpResponse('<h1>Test page</h1>')