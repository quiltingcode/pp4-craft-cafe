from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from .forms import CommentForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy


class PostList(generic.ListView):
    # login_url = '/accounts/login/'
    # redirect_field_name = '/craft-community'
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'craft-community.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['form'] = PostForm()
        context['photos'] = Post.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        filtered_posts = Post.objects.all()
        chosen_filter = self.request.GET.get('category-filter')
        if chosen_filter and chosen_filter != "All":
            filtered_posts = filtered_posts.filter(category=chosen_filter)
            print(filtered_posts)
        return render(request, "craft-community.html", {"filtered_posts": filtered_posts, 'selected': chosen_filter, 'categories': Post.objects.all().order_by('category')})

    def post(self, request):
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.instance.email = request.user.email
            post_form.instance.name = request.user.username
            post = post_form.save(commit=False)
            post.author = self.request.user
            post.status = 1
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post submitted successfully, awaiting approval.')
        else:
            post_form = PostForm()

        return redirect('craft-community')


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
        return redirect('craft-community')


class EditPost(UpdateView):
    model = Post
    template_name = 'edit-post.html'
    fields = ['title', 'category', 'featured_image', 'content']
    success_url = '/contact/profile-page'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('profile-page')


class EditComment(UpdateView):
    model = Comment
    template_name = 'edit-comment.html'
    fields = ['comment_content']
    success_url = '/contact/profile-page'


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'delete-comment.html'
    success_url = reverse_lazy('profile-page')


class AdminPostApproval(UpdateView):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.approved:
            post.approved = False
            post.save()
            messages.add_message(
                request, messages.SUCCESS, 'Post Unapproved')
        else:
            post.approved = True
            post.save()
            messages.add_message(
                request, messages.SUCCESS, 'Post approved')
        return redirect('cafe-dashboard')


class AdminCommentApproval(UpdateView):

    def post(self, request, id):
        comment = get_object_or_404(Comment, id=id)

        if comment.approved:
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment Unapproved')
        else:
            comment.approved = True
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment approved')
        return redirect('cafe-dashboard')


class AdminEditPost(UpdateView):
    model = Post
    template_name = 'admin-edit-post.html'
    fields = ['title', 'category', 'featured_image', 'content', 'approved']
    success_url = reverse_lazy('cafe-dashboard')