from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator

from property_web.models import BaseModel


class User(AbstractBaseUser, BaseModel):
    """
    A custom user model with phone number field.

    This model is used to represent users in the system. It inherits from
    Django's built-in AbstractBaseUser and also includes some additional fields
    from the BaseModel.

    Attributes:
        phone_number (str): The phone number of the user. Must be a 10-digit
            number starting with '0'. This field is unique across all users.
    """

    phone_number = models.CharField(
        validators=[RegexValidator(r"^0\d{9}$")], max_length=10, unique=True
    )

    def __str__(self):
        """
        Return a string representation of the User object.
        """

        return str(self.username)
