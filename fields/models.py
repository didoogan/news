from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class CommonField(models.Model):

    POSITION_CHOICE = [
        ('static', 'static'),
        ('relative', 'relative'),
        ('fixed', 'fixed'),
        ('absolute', 'absolute')
    ]

    name = models.CharField(max_length=30)

    margin_left = models.CharField(max_length=10, blank=True, default='auto')
    margin_top = models.CharField(max_length=10, blank=True, default='auto')
    margin_right = models.CharField(max_length=10, blank=True, default='auto')
    margin_bottom = models.CharField(max_length=10, blank=True, default='auto')

    padding_left = models.CharField(max_length=10, blank=True, default='auto')
    padding_top = models.CharField(max_length=10, blank=True, default='auto')
    padding_right = models.CharField(max_length=10, blank=True, default='auto')
    padding_bottom = models.CharField(max_length=10, blank=True, default='auto')

    position = models.CharField(max_length=9, choices=POSITION_CHOICE, default='static')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class TextField(CommonField):

    FONT_FAMILY_CHOICE = [
        ('Times New Roman', 'Times New Roman'),
        ('Georgia', 'Georgia'),
        ('Times', 'Times'),
        ('Arial', 'Arial'),
        ('Helvetica', 'Helvetica')
    ]
    GENERIC_FAMILY_CHOICE = [
        ('serif', 'serif'),
        ('sans-serif', 'sans-serif'),
        ('cursive', 'cursive'),
        ('fantasy', 'fantasy'),
        ('monospace', 'monospace')
    ]

    font_size = models.CharField(max_length=15, default='12px')
    font_family = models.CharField(max_length=20, choices=FONT_FAMILY_CHOICE, default='Arial')
    generic_family = models.CharField(max_length=10, choices=GENERIC_FAMILY_CHOICE, default='serif')
    italic = models.BooleanField(default=False)
    bold = models.BooleanField(default=False)
    color = models.CharField(max_length=15, default='Black')


class Article(models.Model):
    pub_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=200)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL)
    fields = models.ManyToManyField(TextField, through='ArticleItem')

    def __str__(self):
        return '{}...'.format(self.title[:20])


class ArticleItem(models.Model):
    article = models.ForeignKey(Article)
    field = models.ForeignKey(TextField)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.article.title
