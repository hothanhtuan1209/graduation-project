from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.forms import (
    PasswordChangeForm,
    AuthenticationForm,
)
from django.contrib import messages

from .forms import SignUpForm


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


class UserLoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthenticationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

        context = self.get_context_data(**kwargs)
        context["form"] = form

        return self.render_to_response(context)


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
