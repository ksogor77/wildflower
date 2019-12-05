from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt

from .models import Profile, Article, Blog

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

def blog_view(request):
    return render(request, 'blog_view.html')

def blog_create(request):
    return render(request, 'blog_create.html')

########## Auth Pages ##################

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')
