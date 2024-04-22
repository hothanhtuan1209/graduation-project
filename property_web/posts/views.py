from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostForm, ImageForm
from .models import Post
from users.models import CustomUser
from images.models import Image
from property_web.constants.enum import Status
from .helpers.build_query_filter import build_query_filter
from property_web.settings import PAGE_SIZE
from property_web.views import BaseView


class CreatePostView(LoginRequiredMixin, BaseView):
    template_name = 'create_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = PostForm()
        context['image_form'] = ImageForm()

        return context

    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            images = request.FILES.getlist("image")
            image_instances = [Image(post=post, image=image) for image in images]
            Image.objects.bulk_create(image_instances)

            user_id = request.user.id
            return redirect(reverse('user_detail', kwargs={'user_id': user_id}))

        context = self.get_context_data(**kwargs)
        context['post_form'] = post_form
        context['image_form'] = image_form
        return context


class ListPostView(BaseView):
    template_name = 'list_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request_data = self.request.GET
        query_filter = build_query_filter(request_data)
        order_by = request_data.get("order_by", "-created_at")

        posts = (
            Post.objects.filter(Q(status=Status.AVAILABLE.value) & query_filter)
            .order_by(order_by)
            .values("id", "title", "price", "address", "area")
        )

        order_by_selected = request_data.get('order_by')
        paginator = Paginator(posts, PAGE_SIZE)
        page = self.request.GET.get("page", 1)

        try:
            posts_page = paginator.page(page)
        except (PageNotAnInteger, EmptyPage):
            posts_page = paginator.page(1)

        post_ids = [post["id"] for post in posts_page]
        images = Image.objects.filter(post_id__in=post_ids)
        image_mapping = {image.post_id: image.image.url for image in images}

        for post in posts_page:
            post["image"] = image_mapping.get(post["id"])

        context = {
            "posts": posts_page,
            "order_by_selected": order_by_selected
        }
        return context


class PostDetailView(BaseView):
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get('post_id')

        post = get_object_or_404(Post, pk=post_id)
        post_images = post.image_set.all()

        user_post = (
            CustomUser.objects.filter(pk=post.user_id)
            .values("username", "phone_number", "id")
            .get()
        )

        posts_of_user = (
            Post.objects.filter(Q(status=Status.AVAILABLE.value) & Q(user=user_post["id"]))
            .exclude(id=post_id)
            .order_by("-created_at")
            .values("id", "title", "address")[:5]
        )

        post_ids = [post["id"] for post in posts_of_user]
        images = Image.objects.filter(post_id__in=post_ids)
        image_mapping = {image.post_id: image.image.url for image in images}

        for post_user in posts_of_user:
            post_user["image"] = image_mapping.get(post_user["id"])

        context = {
            "post": post,
            "post_images": post_images,
            "user_post": user_post,
            "posts_of_user": posts_of_user,
        }

        return context


class UpdatePostView(LoginRequiredMixin, BaseView):
    template_name = 'edit_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        images_urls = [image.image.url for image in Image.objects.filter(post=post)]

        context = {
            "post_form": PostForm(instance=post),
            "image_form": ImageForm(),
            "images_urls": images_urls
        }

        return context

    def post(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')

        post = get_object_or_404(Post, id=post_id)
        post_form = PostForm(request.POST, instance=post)
        image_form = ImageForm(request.POST, request.FILES, instance=post)

        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save()
            images = request.FILES.getlist("image")

            for image in images:
                Image.objects.create(post=post, image=image)
            return redirect(reverse("post_detail", kwargs={"post_id": post.id}))

        context = self.get_context_data(**kwargs)
        context = {
            "post_form": PostForm(instance=post),
            "image_form": ImageForm(),
        }
        return self.render_to_response(context)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    View function to delete a post.
    """
    model = Post
    template_name = 'posts/templates/post_confirm_delete.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['post_id'])

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'user_id': self.request.user.id})
