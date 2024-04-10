from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from posts.models import Post
from images.models import Image
from property_web.constants.enum import Status


@csrf_exempt
def home_page(request):
    """
    View function to display a list of posts categorized as hot and normal.
    """

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
    context = {"hot_posts": hot_posts, "normal_posts": normal_posts}
    return render(request, "home.html", context)
