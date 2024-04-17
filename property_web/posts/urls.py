from django.urls import path
from .views import CreatePostView, PostDetailView, UpdatePostView, ListPostView, delete_post

urlpatterns = [
    path('', ListPostView.as_view(), name='list_posts'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('<str:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('<str:post_id>/update/', UpdatePostView.as_view(), name='update_post'),
    path('<str:post_id>/delete/', delete_post, name='delete_post'),
]
