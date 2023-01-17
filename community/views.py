from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import TemplateView


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'craft-community.html'
    paginate_by = 6


class HomeView(TemplateView):
    template_name = 'index.html'
