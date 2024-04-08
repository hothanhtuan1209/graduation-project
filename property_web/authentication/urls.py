from django.urls import path
from .views import (
    user_signup,
    user_login,
    change_password,
    user_logout,
    home
    )

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('changepassword/', change_password, name='change_password'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home')
]
