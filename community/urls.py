from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("craft-community/", views.PostList.as_view(), name="community"),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post-detail'),
]
