from . import views
from django.urls import path
from community.views import EditPost, DeletePost

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("craft-community/", views.PostList.as_view(), name="craft-community"),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post-detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('like2/<slug:slug>', views.PostLike2.as_view(), name='post_like2'),
    path('edit-post/<int:pk>', EditPost.as_view(), name='edit-post'),
    path('delete-post/<int:pk>', DeletePost.as_view(), name='delete-post'),
]
