from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_view_paginator(model, page_number=1, count=50, filters={},
                       ordering='-created_on'):
    """Gets a Paginator object from a resulting Queryset applied to given
    Model class.

    Attributes:
        model: Model class from which to build resulting Queryset.
        page_number: Page number to paginate resulting Paginator object.
        count: Max number of items per page in Paginator object.

    Returns:
        paginator: Paginator object.

    """

    items = model.objects.filter(**filters).order_by(ordering)
    paginator = Paginator(items, count)

    try:
        paginator = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = paginator.page(1)
    except EmptyPage:
        # If page is out of ran deliver last page of results.
        paginator = paginator.page(paginator.num_pages)

    return paginator