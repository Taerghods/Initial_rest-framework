from weblog.models import *
from rest_framework import serializers




class ArticleSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'category', 'category_name', 'created_at', 'updated_at', 'published']

class CategorySerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'articles']