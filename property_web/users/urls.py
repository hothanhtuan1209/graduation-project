from django.urls import path
from .views import user_detail, update_user


urlpatterns = [
    path('detail/<str:user_id>/', user_detail, name='user_detail'),
    path('detail/<str:user_id>/edit/', update_user, name='update_user')
]
