from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.datetime_safe import datetime
from accounts.models import *

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(20)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="article")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title