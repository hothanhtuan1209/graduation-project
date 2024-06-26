from django.views.generic import TemplateView

from posts.models import Post
from images.models import Image
from property_web.constants.enum import Status


class BaseView(TemplateView):
    """
    Base view class to contain common functionality shared by other views.
    """

    def get_context_data(self, **kwargs):
        """
        A helper method to get the current logged-in user.
        """
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        return context


class HomePageView(BaseView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = (
            Post.objects.filter(status=Status.AVAILABLE.value)
            .values("id", "title", "price", "address", "hot_post")
            .order_by("-created_at")
        )

        post_ids = [post["id"] for post in posts]
        images = Image.objects.filter(post_id__in=post_ids)
        image_mapping = {image.post_id: image.image.url for image in images}

        for post in posts:
            post["image"] = image_mapping.get(post["id"])

        hot_posts = [post for post in posts if post["hot_post"]][:10]
        normal_posts = [post for post in posts if not post["hot_post"]][:10]

        context["hot_posts"] = hot_posts
        context["normal_posts"] = normal_posts

        return context
