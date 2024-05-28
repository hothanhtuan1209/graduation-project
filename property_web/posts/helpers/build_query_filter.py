from django.db.models import Q

# Define mapping for price range
price_dict = {
    'lt_2m': Q(price__lt=2000000),
    '2m_to_3m': Q(price__range=(2000000, 3000000)),
    'gt_3m': Q(price__gt=3000000)
}

# Define mapping for area range
area_dict = {
    'lt_15': Q(area__lt=15),
    '15_to_25': Q(area__range=(15, 25)),
    'gt_25': Q(area__gt=25)
}


def build_query_filter(request_data):
    """
    Helper function to build the query filter based on various criteria.
    """

    query_filter = Q()

    # Filter by address
    if address := request_data.get('address'):
        query_filter &= Q(address__icontains=address)

    # Filter by price
    if price_range := request_data.get('price_range'):
        query_filter &= price_dict.get(price_range, Q())

    # Filter by area
    if area_range := request_data.get('area_range'):
        query_filter &= area_dict.get(area_range, Q())

    return query_filter
