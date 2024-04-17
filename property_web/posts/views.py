from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import PostForm, ImageForm
from .models import Post
from users.models import CustomUser
from images.models import Image
from property_web.constants.enum import Status
from .helpers.build_query_filter import build_query_filter
from property_web.settings import PAGE_SIZE


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

            images = request.FILES.getlist("images")
            image_instances = [Image(post=post, image=image) for image in images]
            Image.objects.bulk_create(image_instances)

            return redirect("home")
    else:
        post_form = PostForm()
        image_form = ImageForm()

    context = {"post_form": post_form, "image_form": image_form}
    return render(request, "create_post.html", context)


def list_post(request):
    """
    This function to get list all posts have status is AVAILABLE, user can
    filter, search data
    """

    request_data = request.GET
    query_filter = build_query_filter(request_data)
    order_by = request_data.get("order_by", "-created_at")

    posts = (
        Post.objects.filter(Q(status=Status.AVAILABLE.value) & query_filter)
        .order_by(order_by)
        .values("id", "title", "price", "address", "area")
    )

    order_by_selected = request.GET.get('order_by')

    paginator = Paginator(posts, PAGE_SIZE)
    page = request.GET.get("page", 1)

    try:
        posts_page = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        posts_page = paginator.page(1)

    post_ids = [post["id"] for post in posts_page]
    images = Image.objects.filter(post_id__in=post_ids)
    image_mapping = {image.post_id: image.image.url for image in images}

    for post in posts_page:
        post["image"] = image_mapping.get(post["id"])

    context = {
        "posts": posts_page,
        "order_by_selected": order_by_selected
    }

    return render(request, "list_posts.html", context)


def post_detail(request, post_id):
    """
    View function to get detail post by post ID. Addition get
    information user, list post by user ID
    """

    post = get_object_or_404(Post, pk=post_id)
    post_images = post.image_set.all()

    user_post = CustomUser.objects.filter(pk=post.user_id).values('username', 'phone_number', 'id').get()

    posts_of_user = (
        Post.objects.filter(Q(status=Status.AVAILABLE.value) & Q(user=user_post['id']))
            .exclude(id=post_id)
            .order_by("-created_at")
            .values('id', 'title', 'address')[:5]
    )

    post_ids = [post["id"] for post in posts_of_user]
    images = Image.objects.filter(post_id__in=post_ids)
    image_mapping = {image.post_id: image.image.url for image in images}

    for post_user in posts_of_user:
        post_user["image"] = image_mapping.get(post_user["id"])

    context = {
        "post": post,
        "post_images": post_images,
        "user_post": user_post,
        "posts_of_user": posts_of_user,
    }

    return render(request, "post_detail.html", context)


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

    return render(request, "edit_post.html", {"form": form})
