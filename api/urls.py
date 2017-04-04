from django.conf.urls import url, include

urlpatterns = [
    url(r'user/', include('api.user.urls')),
]
