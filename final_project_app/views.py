from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Profile, Article, Blog
from .forms import BlogForm

# Create your views here.

########## Base Pages ###########

def test(request):
    return HttpResponse("Hello Hello")

def landing(request):
    return render(request, 'landing.html')

def article_main(request):
    return render(request, 'article_main.html')

def article_view(request):
    return render(request, 'article_view.html')

def article_create(request):
    return render(request, 'article_create.html')

def blog_main(request):
    return render(request, 'blog_main.html')

def blog_create(request):
    return render(request, 'blog_create.html')

############# Show and Create ###################

@csrf_exempt
def blog_view(request, blog_pk):
    blog = Blog.objects.get(id=blog_pk)
    context = {'title': title, 'body': body}
    return render(request, 'blog_view.html')

@login_required
def blog_create(request):
    if request.method == 'POST':
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST._mutable = mutable
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.creator = request.user
            blog.save()
            return redirect('blog_view', blog_pk=blog.pk)
    else:
        form = BlogForm()
    context = {'form': form, 'header': "Write your blog post here"}
    return render(request, 'blog_create.html', context)

################ Edit and Delete ####################

@login_required
def blog_edit(request, blog_pk):
    blog = Blog.objects.get(id=blog_pk)
    user = request.user
    if request.method == 'POST':
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST._mutable = mutable
        form = BlogForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('blog_view', blog_pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    context = {'form': form, 'header': f"Edit {blog.title}", 'blog': blog, 'user': user}
    return render(request, 'blog_create.html', context)


@login_required
def blog_delete(request, blog_pk):
    blog = Blog.objects.get(id=blog_pk)
    blog.delete()
    return render('blog_main') 