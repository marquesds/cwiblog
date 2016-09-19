from django.contrib import admin
from .models import Post


@admin.register(Post)
class Post(admin.ModelAdmin):
    search_fields = ('title', 'text')
