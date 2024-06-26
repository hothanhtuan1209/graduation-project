from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import (
    PasswordChangeForm,
    AuthenticationForm,
)

from .forms import SignUpForm
from property_web.views import BaseView


class UserSignupView(BaseView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignUpForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

        context = self.get_context_data(**kwargs)
        context['form'] = form

        return self.render_to_response(context)


class UserLoginView(BaseView):
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
        context["error"] = 'Tên đăng nhập hoặc mật khẩu không đúng, vui lòng đăng nhập lại'

        return self.render_to_response(context)


class ChangePasswordView(LoginRequiredMixin, BaseView):
    template_name = 'change_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(self.request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('login')

        context = self.get_context_data(**kwargs)
        context["form"] = form

        return self.render_to_response(context)


class UserLogoutView(LoginRequiredMixin, LogoutView):
    """
    This is function to log out account user
    """

    next_page = 'login'
