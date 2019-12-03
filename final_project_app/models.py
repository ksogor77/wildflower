from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=24)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=24)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class Articles(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey()

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey()

    def __str__(self):
        return self.title

