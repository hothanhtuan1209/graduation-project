from django.urls import path
from .views import (
    user_signup,
    UserLoginView,
    change_password,
    user_logout,
    )

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', user_signup, name='signup'),
    path('changepassword/', change_password, name='change_password'),
    path('logout/', user_logout, name='logout'),
]
