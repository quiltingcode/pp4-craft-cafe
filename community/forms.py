from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'category', 'content',)
