from django import forms
from .models import CustomUser


class UserForm(forms.ModelForm):
    """
    This is form to create a new employee.
    """

    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'email']
