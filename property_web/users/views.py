from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import CustomUser
from .forms import UserForm
from posts.models import Post
from images.models import Image
from property_web.constants.enum import Status


@require_http_methods(["GET"])
def user_detail(request, user_id):
    """
    This function to get detail employee.
    """

    user_detail = get_object_or_404(CustomUser, id=user_id)
    user_posts = (
        Post.objects.filter(
            Q(status=Status.UNAPPROVED.value) | Q(status=Status.AVAILABLE.value),
            user=user_detail.id
        )
        .order_by("-created_at")
        .values('id', 'title', 'address', 'status')[:10]
    )

    post_ids = [post["id"] for post in user_posts]
    images = Image.objects.filter(post_id__in=post_ids)
    image_mapping = {image.post_id: image.image.url for image in images}

    for post in user_posts:
        post["image"] = image_mapping.get(post["id"])

    context = {"user_detail": user_detail, 'user_posts': user_posts}
    return render(request, "detail.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def update_user(request, user_id):
    """
    This function to update information of employee.
    """

    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            detail_url = reverse("user_detail", args=[str(user.id)])
            return redirect(detail_url)
    else:
        form = UserForm(instance=user)

    return render(
        request, "update.html", {"form": form}
    )
