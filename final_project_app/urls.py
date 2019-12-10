from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('article/main/', views.article_main, name='article-main'),
    path('article/view/<int:article_pk>/', views.article_view, name='article-view'),
    path('article/create/', views.article_create, name='article-create'),
    path('article/edit/<int:article_pk>/', views.article_edit, name="article-edit"),
    path('article/delete/<int:article_pk>/', views.article_delete, name="article-delete"),
    path('blog/main/', views.blog_main, name='blog-main'),
    path('blog/view/<int:blog_pk>/', views.blog_view, name='blog-view'),
    path('blog/create/', views.blog_create, name='blog-create'),
    path('blog/edit/<int:blog_pk>/', views.blog_edit, name='blog-edit'),
    path('blog/delete/<int:blog_pk>/', views.blog_delete, name='blog-delete'),
    path('blog/<int:blog_pk>/<int:pk>/comment/', views.comment_create, name='comment-create'),
    path('blog/<int:blog_pk>/<int:pk>/comment/<int:comment_pk>/', views.comment_edit, name='comment-edit'),
    path('blog/<int:blog_pk>/<int:pk>/comment/<int:comment_pk>/', views.comment_delete, name='comment-delete'),
    path('parent-teacher/', views.parent_teacher, name='parent-teacher'),
]