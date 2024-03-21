from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib import messages

from .forms import SignUpForm


def user_signup(request):
    """
    This is function to signup a new user
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


@csrf_exempt
@login_required
def home(request):
    """
    This home page of website
    """

    return render(request, "home.html")
