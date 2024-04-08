from django.urls import path
from .views import create_post, post_list, post_detail, update_post

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('<str:post_id>/', post_detail, name='post_detail'),
    path('edit/<str:post_id>/', update_post, name='update_post'),
    path('', post_list, name='list_post')
]
