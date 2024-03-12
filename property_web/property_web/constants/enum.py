from enum import Enum


class Status(Enum):
    """
    An enumeration representing the status of a property listing.

    Attributes:
        UNAPPROVED (str): The property listing has not been approved.
        FOR_RENT (str): The property is available for rent.
        FULL (str): The property is fully occupied.
    """

    UNAPPROVED = 'UNAPPROVED'
    FOR_RENT = 'FOR_RENT'
    FULL = 'FULL'


class Type(Enum):
    """
    An enumeration representing the type of a property listing.

    Attributes:
        RENT (str): The property is available for rent.
        SALE (str): The property is available for sale.
    """

    RENT = 'RENT'
    SALE = 'SALE'
