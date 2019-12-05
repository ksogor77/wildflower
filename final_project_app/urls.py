from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('article/main/', views.article_main, name='article-main'),
    path('article/view/', views.article_view, name='article-view'),
    path('article/create/', views.article_create, name='article-create'),
    path('blog/main/', views.blog_main, name='blog-main'),
    path('blog/view/<int:blog_pk>', views.blog_view, name='blog-view'),
    path('blog/create/', views.blog_create, name='blog-create'),
]