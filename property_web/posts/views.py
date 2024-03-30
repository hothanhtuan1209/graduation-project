from django.shortcuts import render, redirect
from .forms import PostForm, ImageForm
from .models import Post
from images.models import Image


def create_post(request):
    """
    This view is for creating a new post feature.
    """

    post_form = PostForm(request.POST or None)
    image_form = ImageForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and post_form.is_valid() and image_form.is_valid():
        post = post_form.save(commit=False)
        post.user = request.user
        post.save()

        image = image_form.cleaned_data.get("image")
        if image:
            Image.objects.create(post=post, image=image)

        return redirect("home")

    context = {"post_form": post_form, "image_form": image_form}
    return render(request, "create_post.html", context)
