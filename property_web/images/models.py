from django.db import models
from posts.models import Post


class Image(models.Model):
    """
    This model represents an image uploaded within the system.

    Attributes:
        image (ImageField): The image field, storing the uploaded image.
        post (ForeignKey): A foreign key to the Post model, indicating which
        post this image belongs to.
    """

    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)
