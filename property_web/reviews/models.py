from django.db import models

from property_web.models import BaseModel
from posts.models import Post


class Review(BaseModel):
    """
    Model representing a review associated with a post within the system.

    Attributes:
        - content (TextField): The content of the review.
        - post (ForeignKey): A foreign key to the Post model, indicating which
        post this review is associated with.
    """

    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the Post object.
        """
        return str(self.content)
