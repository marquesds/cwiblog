from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField('Title', max_length=200)
    author = models.ForeignKey(User)
    text = models.TextField('Text', max_length=10000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
