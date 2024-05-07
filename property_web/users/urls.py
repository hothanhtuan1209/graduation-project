from django.urls import path
from .views import UserDetailView, UpdateUserView

urlpatterns = [
    path('<str:user_id>/', UserDetailView.as_view(), name='user_detail'),
    path('<str:user_id>/edit/', UpdateUserView.as_view(), name='update_user')
]
