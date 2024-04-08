from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import PostForm, ImageForm
from .models import Post
from users.models import CustomUser
from images.models import Image


@login_required
def create(request):
    """
    This view is for creating a new post feature.
    """

    if request.method == "POST":
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            images = request.FILES.getlist('images')
            image_instances = [Image(post=post, image=image) for image in images]
            Image.objects.bulk_create(image_instances)

            return redirect("list_post")
    else:
        post_form = PostForm()
        image_form = ImageForm()

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
    user_id = post.user_id
    post_user = get_object_or_404(CustomUser, pk=user_id)
    return render(
        request, 'post_detail.html', {'post': post, 'post_user': post_user}
    )


@require_http_methods(["GET", "POST"])
def update_post(request, post_id):
    """
    View function to update information of a post.
    """

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            detail_url = reverse("post_detail", args=[str(post.id)])
            return redirect(detail_url)
    else:
        form = PostForm(instance=post)

    return render(
        request, "edit_post.html", {"form": form}
    )
