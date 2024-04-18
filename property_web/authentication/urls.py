from django.urls import path
from .views import (
    UserSignupView,
    UserLoginView,
    ChangePasswordView,
    UserLogoutView,
    )

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('changepassword/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
