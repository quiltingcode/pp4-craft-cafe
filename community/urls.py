from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("craft-community/", views.PostList.as_view(), name="community"),
]
