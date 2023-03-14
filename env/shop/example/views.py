from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

# Create your views here.

menu = [{'title': 'О сайте','url_name': 'about'},
        {'title': 'Добавить статью','url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    posts = Example.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'example/index.html', context = context)


def about(request):
    return render(request, 'example/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(requesr, exception):
    return HttpResponseNotFound("<h1>The page you are looking for was not found</h1>")


def show_post(request, post_id):
    return HttpResponse(f'Отобранные страницы с id = {post_id}')