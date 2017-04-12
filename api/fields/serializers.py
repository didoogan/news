from rest_framework import serializers

from fields.models import TextField, Article, ArticleItem


class TextFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextField
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # fields = TextFieldSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleItemSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    field = TextFieldSerializer(read_only=True)

    class Meta:
        model = ArticleItem
        fields = [
            'article',
            'field',
            'content'
        ]
