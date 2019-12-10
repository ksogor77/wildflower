from django.contrib import admin
from .models import Profile, Article, Blog, Comment

admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(Blog)
admin.site.register(Comment)

