from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm, LoginForm, PasswordChangeForm


def user_signup(request):
    """
    This is function to signup a new user
    """

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def user_login(request):
    """
    This is function to login and authenticate user
    """

    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def change_password(request):
    """
    This is function to change password for user
    """

    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']
            if request.user.check_password(old_password) and new_password == confirm_new_password:
                request.user.set_password(new_password)
                request.user.save()
                # Update session to prevent logout after password change
                update_session_auth_hash(request, request.user)
                return redirect('login')
    else:
        form = PasswordChangeForm()
    return render(request, 'change_password.html', {'form': form})


@login_required
def user_logout(request):
    """
    This is function to log out account user
    """

    logout(request)
    return redirect('login')


@csrf_exempt
@login_required
def home(request):
    """
    This home page of website
    """

    return render(request, 'home.html')
