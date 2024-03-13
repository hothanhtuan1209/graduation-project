from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

from property_web.models import BaseModel
from posts.models import Post


class S3MediaStorage(S3Boto3Storage):
    location = 'media'


class Image(BaseModel):
    """
    This model represents an image uploaded within the system.

    Attributes:
        image (ImageField): The image field, storing the uploaded image.
        post (ForeignKey): A foreign key to the Post model, indicating which
        post this image belongs to.
    """

    image = models.ImageField(storage=S3MediaStorage())
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
