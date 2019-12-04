from django.shortcuts import render
from django.http import HttpResponse
# from django.core import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt

from .models import User, Articles, Blog

# Create your views here.

########## Base Pages ###########

def test(request):
    return HttpResponse("Hello Hello")

def landing(request):
    return render(request, 'landing.html')
