from django.urls import path
from .views import create_post, post_list

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('', post_list, name='list_post')
]
