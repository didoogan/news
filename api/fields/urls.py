from rest_framework.routers import DefaultRouter

from .views import TextFieldViewSet, ArticleViewSet, ArticleItemViewSet


router = DefaultRouter()
router.register(r'text_fields', TextFieldViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'article_items', ArticleItemViewSet)

urlpatterns = router.urls
