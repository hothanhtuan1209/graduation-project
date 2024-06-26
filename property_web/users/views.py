from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser
from property_web.views import BaseView
from .forms import UserForm
from posts.models import Post
from images.models import Image
from property_web.constants.enum import Status


class UserDetailView(BaseView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        user_id = self.kwargs.get("user_id")
        user_detail = get_object_or_404(CustomUser, id=user_id)
        user_posts = (
            Post.objects.filter(
                Q(status=Status.UNAPPROVED.value) | Q(status=Status.AVAILABLE.value),
                user=user_detail.id
            )
            .order_by("-created_at")
            .values('id', 'title', 'price', 'area', 'address', 'status')[:10]
        )

        post_ids = [post["id"] for post in user_posts]
        images = Image.objects.filter(post_id__in=post_ids)
        image_mapping = {image.post_id: image.image.url for image in images}

        for post in user_posts:
            post["image"] = image_mapping.get(post["id"])

        context = {"user_detail": user_detail, 'user_posts': user_posts}
        return context


class UpdateUserView(LoginRequiredMixin, BaseView):
    template_name = "update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(CustomUser, id=user_id)
        form = UserForm(instance=user)
        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):
        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(CustomUser, id=user_id)
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            user = form.save()
            detail_url = reverse("user_detail", args=[str(user.id)])
            return redirect(detail_url)

        return self.render_to_response(self.get_context_data())
