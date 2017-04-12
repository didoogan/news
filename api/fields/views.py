from rest_framework import viewsets

from fields.models import TextField, Article, ArticleItem
from .serializers import TextFieldSerializer, ArticleSerializer, ArticleItemSerializer


class TextFieldViewSet(viewsets.ModelViewSet):
    serializer_class = TextFieldSerializer
    queryset = TextField.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleItemViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleItemSerializer
    queryset = ArticleItem.objects.all()
