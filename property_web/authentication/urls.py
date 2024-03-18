from django.urls import path
from .views import user_signup, user_login

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup')
]
