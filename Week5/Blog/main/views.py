from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog, Comment
from django.utils import timezone
from .forms import BlogForm,CommentForm


def posted(request):
    all_items = Blog.objects.all
    return render(request, 'posted.html', {'all_items': all_items})

def post_detail(request, pk):
    item = Blog.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'item': item})

def delete_post(request,pk):
    item = Blog.objects.get(pk=pk)
    item.delete()
    return redirect('posted')


def post_edit(request, pk):
    item = Blog.objects.get(pk=pk)

    if request.method == "POST":
        form = BlogForm(request.POST,instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('post_detail',pk=item.pk)
    else:
        form = BlogForm(instance=item)

    return render(request, 'post_edit.html', {'form': form})

def my_blog(request):
    if request.method == 'POST':
    	form = BlogForm(request.POST or None)


    	if form.is_valid():
    		form.save()
    		all_items = Blog.objects.all
    		return render(request,'my_blog.html',{'all_items': all_items})

    else:
    	all_items = Blog.objects.all
    	return render(request, 'my_blog.html', {'all_items': all_items})
def delete_com(request,pk):
    item = Comment.objects.get(pk=pk)
    pk = item.com_id.pk
    item.delete() 
    return redirect('post_detail', pk=pk)

def add_comment_to_post(request, pk):
    item = Blog.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.com_id = item
            comment.save()
            return redirect('post_detail', pk=item.pk)
    else:
        form = CommentForm()
    return render(request, 'posted.html', {'form': form})
