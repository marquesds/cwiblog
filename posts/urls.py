from django.conf.urls import url
from .views import posts

urlpatterns = [
    url(r'', posts, name='posts')
]
