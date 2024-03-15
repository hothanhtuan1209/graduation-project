from django.db import models

from property_web.models import BaseModel


class Category(BaseModel):
    """
    A model representing a category for properties.

    This model is used to categorize different types of properties, such as
    apartments, houses, or commercial properties.

    Attributes:
        name (str): The name of the category. Must be unique across all
            categories.
    """

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """
        Return a string representation of the Category object.
        """

        return str(self.name)
