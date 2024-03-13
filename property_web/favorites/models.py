from django.db import models

from users.models import User
from posts.models import Post


class Favorite(models.Model):
    """
    Model representing a favorite relationship between a user and a post.

    Attributes:
        - user (ForeignKey): A foreign key to the User model, representing the
        user who favorited the post.
        - post (ForeignKey): A foreign key to the Post model, representing the
        post that was favorited.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return str(self.post.title)
