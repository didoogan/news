from django.contrib import admin

from .models import TextField, Article, ArticleItem

admin.site.register(TextField)
admin.site.register(Article)
admin.site.register(ArticleItem)
