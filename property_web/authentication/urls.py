from django.urls import path
from .views import (
    user_signup,
    user_login,
    change_password,
    user_logout,
    home_page
    )

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('changepassword/', change_password, name='change_password'),
    path('logout/', user_logout, name='logout'),
]
