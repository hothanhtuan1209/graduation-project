from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import CustomUser


@require_http_methods(["GET"])
def user_detail(request, user_id):
    """
    This function to get detail employee.
    """

    user = get_object_or_404(CustomUser, id=user_id)
    context = {'user': user}
    return render(request, 'detail.html', context)
