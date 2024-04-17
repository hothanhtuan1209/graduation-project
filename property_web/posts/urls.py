from django.urls import path
from .views import create, post_detail, update_post, list_post, delete_post

urlpatterns = [
    path('', list_post, name='list_posts'),
    path('create/', create, name='create_post'),
    path('<str:post_id>/', post_detail, name='post_detail'),
    path('<str:post_id>/update', update_post, name='update_post'),
    path('<str:post_id>/delete', delete_post, name='delete_post'),
]
