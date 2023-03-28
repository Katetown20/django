from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *

# Create your views here.

menu = [{'title': 'О сайте','url_name': 'about'},
        {'title': 'Добавить статью','url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]

class ExampleHome(ListView):
    model = Example
    template_name = 'example/index.html'
    context_object_name = 'posts'

#передача динамических и статических данных
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Example.objects.filter(is_published=True)

# def index(request):
#     posts = Example.objects.all()
#
#     context = {
#         'posts': posts,
#
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'example/index.html', context = context)


def about(request):
    return render(request, 'example/about.html', {'menu': menu, 'title': 'О сайте'})


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'example/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'example/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(requesr, exception):
    return HttpResponseNotFound("<h1>The page you are looking for was not found</h1>")


# def show_post(request, post_slug):
#     post = get_object_or_404(Example, slug=post_slug)
#
#     context = {
#         'posts': post,
#         'menu': menu,
#         'title': 'post.title',
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'example/post.html', context=context)

class ShowPost(DetailView):
    model = Example
    template_name = 'example/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


class ExampleCategory(ListView):
    model = Example
    template_name = 'example/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_queryset(self):
        return Example.objects.filter(cat__slug=self.kwargs['cat_slug'],  is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория +' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


# def show_category(request, cat_id):
#     posts = Example.objects.filter(cat_id=cat_id)
#
#
#     if len(posts)  == 0:
#         raise Http404()
#
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение категорий',
#         'cat_selected':  cat_id,
#     }
#     return render(request, 'example/index.html', context=context)