from django.db import models
from datetime import datetime, timedelta

from property_web.models import BaseModel
from property_web.constants.enum import Status, Type
from category.models import Category
from users.models import CustomUser


class Post(BaseModel):
    """
    A model representing a post for a rental property or property for sale.

    This model is used to store information about a property listing, including
    its title, price, area, description, end date, status, type, category, and
    user.

    Attributes:
        - title (str): The title of the property listing.
        - price (int): The price of the property.
        - area (Decimal): The area of the property.
        - description (str): A description of the property.
        - end_date (DateTime): The end date of the property listing.
        - status (str): The status of the property listing, chosen from the
        Status enumeration.
        - type (str): The type of the property listing, chosen from the Type
        enumeration.
        - category (Category): The category of the property listing.
        user (User): The user who posted the property listing.
    """

    title = models.CharField(max_length=200)
    price = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField()
    address = models.CharField(max_length=255)
    hot_post = models.BooleanField(default=False)
    end_date = models.DateTimeField(
        default=datetime.now() + timedelta(days=30)
    )
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.value) for status in Status],
        default=Status.UNAPPROVED.value
    )
    type = models.CharField(
        max_length=10, choices=[(type.value, type.value) for type in Type]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the Post object.
        """
        return str(self.title)
