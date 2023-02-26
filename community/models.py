from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.template.defaultfilters import slugify

STATUS = ((0, "Draft"), (1, "Published"))

WORKSHOP_CATEGORIES = (
    ("All things Wool", "All things Wool"),
    ("Quilting", "Quilting"),
    ("Clothing", "Clothing"),
    ("Home Decor", "Home Decor"),
    ("Needlepoint", "Needlepoint"),
    ("Kids Crafts", "Kids Crafts"),
)


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Title of your Post"
        )
    slug = models.SlugField(max_length=200, null=False, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="community_posts"
    )
    featured_image = CloudinaryField(
        'image',
        default='placeholder',
        )
    category = models.CharField(
        max_length=50,
        choices=WORKSHOP_CATEGORIES,
        default="All Things Wool",
        verbose_name="Choose a Post Category"
        )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name="Describe your crafty creation")
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name='post_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()

    def number_of_posts(self):
        return self.title.count()

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    updated_on = models.DateTimeField(auto_now=True)
    comment_content = models.TextField(verbose_name="Comments")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment_content} by {self.name}"
