from . import views
from django.urls import path
from community.views import EditPost, DeletePost, AdminPostApproval

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("craft-community/", views.PostList.as_view(), name="craft-community"),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post-detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('like2/<slug:slug>', views.PostLike2.as_view(), name='post_like2'),
    path('edit-post/<int:pk>', EditPost.as_view(), name='edit-post'),
    path('delete-post/<int:pk>', DeletePost.as_view(), name='delete-post'),
    path('edit-comment/<int:pk>', views.EditComment.as_view(), name='edit-comment'),
    path('delete-comment/<int:pk>', views.DeleteComment.as_view(), name='delete-comment'),
    path('approve-post/<slug:slug>', views.AdminPostApproval.as_view(), name='approve-post'),
]
