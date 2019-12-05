from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')

    def __str__(self):
        return self.user.username

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_author')

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')

    def __str__(self):
        return self.title

