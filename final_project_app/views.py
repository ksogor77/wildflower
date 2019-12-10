from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import BlogForm, ArticleForm, CommentForm
from .models import Profile, Article, Blog, Comment


# Create your views here.

########## Base Pages ###########

def test(request):
    return HttpResponse("Hello Hello")

def landing(request):
    return render(request, 'landing.html')

def parent_teacher(request):
    return render(request, 'parent-teacher.html')


############# Blog Show and Create ###################
def blog_main(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog_main.html', context)

@csrf_exempt
def blog_view(request, blog_pk, comment_pk):
    blog = Blog.objects.get(id=blog_pk)
    form = CommentForm()
    comment = Comment.objects.get(id=comment_pk)
    context = {'blog': blog, 'form': form, 'comment': comment}
    return render(request, 'blog_view.html', context)

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user_name = request.user
            blog.save()
            return redirect('blog-view', blog_pk=blog.pk)
    else:
        form = BlogForm()
    context = {'form': form, 'header': "Write your blog post here"}
    return render(request, 'blog_create.html', context)

################ Blog Edit and Delete ####################

@login_required
def blog_edit(request, blog_pk):
    blog = Blog.objects.get(id=blog_pk)
    blog.user_name = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog-view', blog_pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    context = {'form': form, 'header': f"Edit {blog.title}", 'blog': blog}
    return render(request, 'blog_create.html', context)


@login_required
def blog_delete(request, blog_pk):
    blog = Blog.objects.get(id=blog_pk)
    blog.delete()
    return render(request, 'blog_main.html') 

############# Article Show and Create ########################

def article_main(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'article_main.html', context)

@csrf_exempt
def article_view(request, article_pk):
    article = Article.objects.get(id=article_pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user_name = request.user
            article.save()
            return redirect('article-view', article_pk=article.pk)
    else:
        form = ArticleForm()
    context = {'form': form, 'header': "Write your article here"}
    return render(request, 'article_create.html', context)


############## Article Edit and Delete ######################

@login_required
def article_edit(request, article_pk):
    article = Article.objects.get(id=article_pk)
    article.user_name = request.user
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('article-view', article_pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form, 'header': f"Edit {article.title}", 'article': article}
    return render(request, 'article_create.html', context)

@login_required
def article_delete(request, article_pk):
    article = Article.objects.get(id=article_pk)
    article.delete()
    return render(request, 'article_main.html') 

########### Comments ####################

@csrf_exempt
def comment_view(request, pk, blog_pk, comment_pk):
    user = User.objects.get(id=pk)
    blog = Blog.objects.get(id=blog_pk)
    comment = Comment.objects.get(id=comment_pk)
    context = {'comment': comment}
    return render(request, 'blog_view.html', context)

@login_required
def comment_create(request, pk, blog_pk):
    user = User.objects.get(id=pk)
    blog = Blog.objects.get(id=blog_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_name = request.user
            comment.blog_id = request.user
            comment.save()
            return redirect('blog-view', blog_pk=blog.pk)
    else:
        form = CommentForm()
    return redirect('blog-view', blog_pk=blog.pk)

@login_required
def comment_edit(request, pk, blog_pk, comment_pk):
    user = User.objects.get(id=pk)
    blog = Blog.objects.get(id=blog_pk)
    comment = Comment.objects.get(id=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('blog-view', blog_pk=blog.pk)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form, 'comment': comment}
    return render(request, 'blog-create.html', context)


@login_required
def comment_delete(request, pk, blog_pk, comment_pk):
    user = User.objects.get(id=pk)
    blog = Blog.objects.get(id=blog_pk)
    comment = Comment.objects.get(id=comment_pk)
    comment.delete()
    return render(request, 'blog_main.html') 
