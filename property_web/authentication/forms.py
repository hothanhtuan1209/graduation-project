from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        label='Old Password', widget=forms.PasswordInput
    )
    new_password = forms.CharField(
        label='New Password', widget=forms.PasswordInput
    )
    confirm_new_password = forms.CharField(
        label='Confirm New Password', widget=forms.PasswordInput
    )
