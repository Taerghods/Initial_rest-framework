from django.contrib import admin
from weblog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'content', 'author', 'created_at', 'updated_at', 'published']