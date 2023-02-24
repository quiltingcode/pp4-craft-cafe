from . import views
from django.urls import path
from community.views import EditPost, DeletePost, AdminPostApproval
from community.views import AdminCommentApproval, AdminEditPost
from community.views import AdminEditComment, AdminDeleteComment
from community.views import AdminDeletePost

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("craft-community/", views.PostList.as_view(), name='craft-community'),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post-detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('like2/<slug:slug>', views.PostLike2.as_view(), name='post_like2'),
    path('edit-post/<int:pk>', EditPost.as_view(), name='edit-post'),
    path(
        'admin-edit-post/<int:pk>',
        AdminEditPost.as_view(),
        name='admin-edit-post'
        ),
    path('delete-post/<int:pk>', DeletePost.as_view(), name='delete-post'),
    path(
        'admin-delete-post/<int:pk>',
        AdminDeletePost.as_view(),
        name='admin-delete-post'
        ),
    path(
        'edit-comment/<int:pk>',
        views.EditComment.as_view(),
        name='edit-comment'
        ),
    path(
        'admin-edit-comment/<int:pk>',
        views.AdminEditComment.as_view(),
        name='admin-edit-comment'
        ),
    path(
        'delete-comment/<int:pk>',
        views.DeleteComment.as_view(),
        name='delete-comment'
        ),
    path(
        'admin-delete-comment/<int:pk>',
        views.AdminDeleteComment.as_view(),
        name='admin-delete-comment'
        ),
    path(
        'approve-post/<slug:slug>/approve',
        views.AdminPostApproval.as_view(),
        name='approve-post'
        ),
    path(
        'approve/<int:id>/comment',
        views.AdminCommentApproval.as_view(),
        name='approve-comment'
        ),
]
