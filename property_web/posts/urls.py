from django.urls import path
from .views import create_post, post_list, post_detail, update_post

urlpatterns = [
    path('', post_list, name='list_post'),
    path('create/', create_post, name='create_post'),
    path('<str:post_id>/', post_detail, name='post_detail'),
    path('<str:post_id>/update', update_post, name='update_post'),
]
