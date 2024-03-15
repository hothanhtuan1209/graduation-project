from enum import Enum


class Status(Enum):
    """
    An enumeration representing the status of a property listing.

    Attributes:
        UNAPPROVED (str): The property listing has not been approved.
        AVAILABLE (str): The property has vacant rooms available.
        OCCUPIED (str): The property is fully occupied.
    """

    UNAPPROVED = 'UNAPPROVED'
    AVAILABLE = 'AVAILABLE'
    OCCUPIED = 'OCCUPIED'


class Type(Enum):
    """
    An enumeration representing the type of a property listing.

    Attributes:
        RENT (str): The property is available for rent.
        SALE (str): The property is available for sale.
    """

    RENT = 'RENT'
    SALE = 'SALE'
