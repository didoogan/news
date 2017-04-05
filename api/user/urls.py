from django.conf.urls import include, url
from rest_framework import routers

from .views import UserViewSet, get_csrf

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'get_csrf/$', get_csrf),
]

urlpatterns += router.urls
