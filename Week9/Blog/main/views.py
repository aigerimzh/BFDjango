from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Blog, Comment
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.utils import timezone
from .forms import BlogForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home.html'
    http_method_names = ['get']

class ArticlList(ListView):
    model = Blog
    context_object_name = 'items'

class ArticleDetail(DetailView):
    model = Blog


class ArticleDelete(DeleteView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('blog_list')

    def get_queryset(self):
        return Blog.objects.for_user(user=self.request.user)

class ArticleUpdate(UpdateView, LoginRequiredMixin):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog_list')
    template_name_suffix = '_update_form'

    def get_queryset(self):
        return Blog.objects.for_user(user=self.request.user)

class ArticleCreate(CreateView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('blog_list')
    fields = ["id","tit_bl","createted_at","text_bl"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class CommentCreate(CreateView):
    model = Comment
    fields = ["com_id","user", "text_com"]



class CommentList(ListView):
    model = Comment
    context_object_name = 'comments'


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('blog_list')



