from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import (
    PasswordChangeForm,
    AuthenticationForm,
)
from django.contrib import messages

from .forms import SignUpForm
from posts.models import Post
from images.models import Image
from property_web.constants.enum import Status


def user_signup(request):
    """
    This function handles user sign up.
    """

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


def user_login(request):
    """
    This function handles user login and authentication.
    """

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
        else:
            return render(
                request,
                "login.html",
                {
                    "form": form,
                    "error": "Username or password is incorrect, please re-enter",
                },
            )

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


@csrf_exempt
def home_page(request):
    """
    View function to display a list of posts categorized as hot and normal.
    """

    hot_posts = (
        Post.objects.filter(status=Status.AVAILABLE.value, hot_post=True)
        .values("id", "title", "price", "address")
        .order_by("-created_at")[:10]
    )

    normal_posts = (
        Post.objects.filter(status=Status.AVAILABLE.value, hot_post=False)
        .values("id", "title", "price", "address")
        .order_by("-created_at")[:10]
    )

    post_ids = [post["id"] for post in hot_posts] + [
        post["id"] for post in normal_posts
    ]
    images = Image.objects.filter(post_id__in=post_ids)
    image_mapping = {image.post_id: image.image.url for image in images}

    for post in hot_posts:
        post["image"] = image_mapping.get(post["id"])

    for post in normal_posts:
        post["image"] = image_mapping.get(post["id"])

    context = {"hot_posts": hot_posts, "normal_posts": normal_posts}
    return render(request, "home.html", context)


@login_required
def change_password(request):
    """
    This is function to change password for user
    """

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("login")
        else:
            messages.error(request, "Please correct the error below.")

    else:
        form = PasswordChangeForm(request.user)

    return render(request, "change_password.html", {"form": form})


@login_required
def user_logout(request):
    """
    This is function to log out account user
    """

    logout(request)
    return redirect("login")
