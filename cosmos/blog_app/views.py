from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from uni_app.models import Cat
from .models import *
# Create your views here.

@login_required(login_url='auth:login')
def blog_view(request): 

    if request.method=='POST':
        post = request.POST.get("post")
        content = request.POST.get("comment")
        user = request.user;
        Comment.objects.create(post=Post.objects.get(id=post), content=content, author=user)
        return redirect('blog:view')
    
    ctx = {"cats":Cat.objects.order_by("name")}

    posts = Post.objects.order_by("-date")

    paginator = Paginator(posts, 2)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    ctx["posts"]=posts

    return render(request, 'blog.html', ctx)


@login_required(login_url='auth:login')
def make_view(request): 

    if request.method=='POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        topics = request.POST.getlist("topics")
        user = request.user;
        p = Post.objects.create(title=title, content=content, author=user)
        p.topic.set(topics)
        return redirect('blog:view')
    
    ctx = {"cats":Cat.objects.order_by("name"), "topics":Topic.objects.order_by("name")}

    return render(request, 'make.html', ctx)