from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Topic(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self): return f"{self.name}"
    class Meta: verbose_name="Topic"; verbose_name_plural="Topics"

class Post(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    topic = models.ManyToManyField(Topic)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): return f"{self.title} : {self.author.username}"
    

class Comment(models.Model):

    # author, content, date
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self): return f"{self.author.username} on {self.post.title}"

