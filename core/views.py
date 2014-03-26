from django.shortcuts import render, RequestContext
from django.http import HttpResponse


def index(request):
    """This view serves an index page showing all the WikiPage instances in the
    system.

    Attributes:
        request: HttpRequest object representing the current request object.

    Returns:
        response: HttpResponse object used to render index page using
            index.html page.
    """

    return render(request, 'index.html')


def view_page(request, page_url):
    """

    """

    return HttpResponse('This is the Page')


def edit_page(request, page_url):
    """

    """

    return HttpResponse('Edit this page!')


def changelog_view(request):
    """

    """

    return HttpResponse('This is our change log.')