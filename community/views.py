from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from django.views.generic import TemplateView
from .forms import CommentForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class PostList(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    redirect_field_name = '/craft-community'
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'craft-community.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.email = request.user.email
            post_form.instance.name = request.user.username
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post submitted successfully, awaiting approval.')
        else:
            post_form = PostForm()

        return render(
            request,
            "craft-community.html",
            {
                "post": post,
                "post_form": PostForm()
            },
        )


class HomeView(TemplateView):
    template_name = 'index.html'


class PostDetails(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post-detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment posted successfully, awaiting approval.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post-detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post-detail', args=[slug]))


class PostLike2(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('craft-community', args=[slug]))


class ProfilePagePosts(generic.ListView):
    def get(self, request):
        model = Post
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        user_posts = post.filter(user=request.user)
        context = {
            'user_posts': user_posts
        }
        template_name = "profile-page.html"
        paginate_by = 10
        return render(
            request,
            "profile-page.html",
            context
        )

    def get(self, request):
        model = Comment
        comments = Comment.objects.filter(user=request.user)
        context = {
            'comments': comments
        }
        template_name = "profile-page.html"
        paginate_by = 10
        return render(
            request,
            "profile-page.html",
            context
        )
