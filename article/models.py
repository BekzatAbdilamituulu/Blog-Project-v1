from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(default=now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()
    category = models.ForeignKey('Category', related_name='category', on_delete=models.PROTECT)
    def get_absolute_url(self):
        return reverse('article:detail', args=[str(self.id)])
    
    def __str__(self) -> str:
        return self.title
    
class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)


    def get_absolute_url(self):
        return reverse('article:category', kwargs={'cat_id': self.pk})

    def __str__(self) -> str:
        return self.name
    
