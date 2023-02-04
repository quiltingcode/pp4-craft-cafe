from . import views
from django.urls import path
from community.views import ProfilePagePosts

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("craft-community/", views.PostList.as_view(), name="craft-community"),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post-detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('like/<slug:slug>', views.PostLike2.as_view(), name='post_like2'),
    path('profile-page', ProfilePagePosts.as_view(), name='profile-page'),
]
