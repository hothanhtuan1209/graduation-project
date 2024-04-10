from django.db.models import Q


def build_query_filter(request_data):
    """
    Helper function to build the query filter based on various criteria.
    """

    query_filter = Q()

    # Mapping for price range
    price_dict = {
        'lt_2m': Q(price__lt=2000000),
        '2m_to_3m': Q(price__range=(2000000, 3000000)),
        'gt_3m': Q(price__gt=3000000)
    }

    # Mapping for area range
    area_dict = {
        'lt_15': Q(area__lt=15),
        '15_to_25': Q(area__range=(15, 25)),
        'gt_25': Q(area__gt=25)
    }

    # Filter by address
    address = request_data.get('address')
    if address:
        query_filter &= Q(address__icontains=address)

    # Filter by price
    price_range = request_data.get('price_range')
    if price_range:
        price_filter = price_dict.get(price_range)
        if price_filter:
            query_filter &= price_filter

    # Filter by area
    area_range = request_data.get('area_range')
    if area_range:
        area_filter = area_dict.get(area_range)
        if area_filter:
            query_filter &= area_filter

    return query_filter
