from django.urls import path
from .views import user_detail


urlpatterns = [
    path('detail/<str:user_id>/', user_detail, name='user_detail'),
]
