from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse

from .models import CustomUser
from .forms import UserForm


@require_http_methods(["GET"])
def user_detail(request, user_id):
    """
    This function to get detail employee.
    """

    user = get_object_or_404(CustomUser, id=user_id)
    user_post = user.post_set.all()
    context = {"user": user, 'user_posts': user_post}
    return render(request, "detail.html", context)


@require_http_methods(["GET", "POST"])
def update_user(request, user_id):
    """
    This function to update information of employee.
    """

    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            detail_url = reverse("user_detail", args=[str(user.id)])
            return redirect(detail_url)
    else:
        form = UserForm(instance=user)

    return render(
        request, "update.html", {"form": form}
    )
