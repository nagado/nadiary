from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Posts.as_view(), name='posts'),
    url(r'^new$', views.NewPost.as_view(), name='new'),
]
