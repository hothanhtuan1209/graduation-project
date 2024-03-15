import uuid
from django.db import models


class BaseModel(models.Model):
    """
    A base model with 'create_at' and 'id' fields to track the creation
    time and unique identifier of objects.

    Attributes:
        create_at (DateTimeField): A field to store the creation time of
        objects.
        id (UUIDField): A field to store a unique identifier (UUID) for each
        object.
        archived (BooleanField): A field to indicate whether the object is
        archived (deleted) or not.
        modified_at (DateTimeField): A field to store the last modification
        time of objects.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    archived = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
