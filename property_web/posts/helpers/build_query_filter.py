from django.db.models import Q


def build_query_filter(request_data):
    """
    Helper function to build the query filter based on various criteria.
    """

    query_filter = Q()

    # Filter by address
    address = request_data.get('address')
    if address:
        query_filter &= Q(address__icontains=address)

    # Filter by price
    price_range = request_data.get('price_range')
    if price_range:
        if price_range == 'lt_2m':
            query_filter &= Q(price__lt=2000000)
        elif price_range == '2m_to_3m':
            query_filter &= Q(price__range=(2000000, 3000000))
        elif price_range == 'gt_3m':
            query_filter &= Q(price__gt=3000000)

    # Filter by area
    area_range = request_data.get('area_range')
    if area_range:
        if area_range == 'lt_15':
            query_filter &= Q(area__lt=15)
        elif area_range == '15_to_25':
            query_filter &= Q(area__range=(15, 25))
        elif area_range == 'gt_25':
            query_filter &= Q(area__gt=25)

    return query_filter
