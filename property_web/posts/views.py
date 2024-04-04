from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PostForm, ImageForm
from .models import Post
from images.models import Image


def create_post(request):
    """
    This view is for creating a new post feature.
    """

    post_form = PostForm(request.POST or None)
    image_form = ImageForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and post_form.is_valid() and image_form.is_valid():
        post = post_form.save(commit=False)
        post.user = request.user
        post.save()

        image = image_form.cleaned_data.get("image")
        if image:
            Image.objects.create(post=post, image=image)

        return redirect("list_post")

    context = {"post_form": post_form, "image_form": image_form}
    return render(request, "create_post.html", context)


def post_list(request):
    """
    View function to display a list of posts categorized as hot and normal.
    """

    hot_posts = Post.objects.filter(
        hot_post=True, status='AVAILABLE'
    ).order_by("-created_at")
    normal_posts = Post.objects.filter(
        hot_post=False, status='AVAILABLE'
    ).order_by("-created_at")

    context = {"hot_posts": hot_posts, "normal_posts": normal_posts}
    return render(request, "list_posts.html", context)


def post_detail(request, post_id):
    """
    View function to get detail post by post ID
    """

    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})
