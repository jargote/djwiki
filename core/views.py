from django.core import exceptions
from django.shortcuts import render, HttpResponseRedirect, urlresolvers

from core import utils
from core.models import WikiPage, Changelog


def index(request):
    """This view serves an index page showing all the WikiPage instances in the
    system.

    Attributes:
        request: HttpRequest object representing the current request object.

    Returns:
        response: HttpResponse object used to render index page using
            index.html page.
    """

    page_number = request.GET.get('page', 1)
    wikipages = utils.get_view_paginator(WikiPage, page_number, 10)

    return render(request, 'index.html', {'title': 'Index',
                                          'wikipages': wikipages})


def view_page(request, page_url):
    """This view will display a WikiPage.

    If page_url does not match any of the stored WikiPage urls then a "Page Do
    Not exist" page will be displayed. This page also contains a link to create
    this new page.

    Attributes:
        request: HttpRequest object representing the current request object.
        page_url: WikiPage url.

    Returns:
        response: HttpResponse object used to render index page using
            wikipage.html page.
    """

    try:
        # Trying to fetch wiki page given its page url.
        wikipage = WikiPage.objects.get(url=page_url)
    except exceptions.ObjectDoesNotExist:
        wikipage = WikiPage(url=page_url)

    return render(request, 'wikipage.html', {'title': wikipage.title,
                                             'wikipage': wikipage})


def edit_page(request, page_url):
    """This view will display a form to edit the body of a WikiPage instance.

    If page_url does not match any of the stored WikiPage url then a new
    instance will be created.

    Attributes:
        request: HttpRequest object representing the current request object.
        page_url: WikiPage url.

    Returns:
        response: HttpResponse object used to render index page using
            wikipage_edit.html page.
    """


    try:
        # Trying to fetch wiki page given its page url.
        wikipage = WikiPage.objects.get(url=page_url)
    except exceptions.ObjectDoesNotExist:
        wikipage = WikiPage.objects.create(
            url=page_url, markdown=utils.get_markdown_filename(page_url))

    return render(request, 'wikipage_edit.html', {'title': wikipage.title,
                                                  'wikipage': wikipage})


def changelog(request, page_url=None):
    """This view display a change log for a given WikiPage or
    all change logs in djwiki.

    Attributes:
        request: HttpRequest object representing the current request object.
        page_url: WikiPage url, maybe None.

    Returns:
        response: HttpResponse object used to render index page using
            changelog.html page.

    """

    title = 'Global History'
    page_number = request.GET.get('page', 1)

    # If page_url is present ChangeLog entries for given WikiPage should be
    # displayed instead.
    if page_url:
        try:
            # Trying to fetch wiki page given its page url.
            wikipage = WikiPage.objects.get(url=page_url)
            title = '"%s" History' % wikipage.title
        except exceptions.ObjectDoesNotExist:
            # Redirect response to wikipage edit view.
            return HttpResponseRedirect(
                urlresolvers.reverse('edit_page', args=[page_url]))
        else:
            # Filter ChangeLog entries for a WikiPage instance.
            changelogs = utils.get_view_paginator(Changelog, page_number, 50,
                                                  wikipage=wikipage)
    else:
        # Return all ChangeLog instances in djwiki.
        changelogs = utils.get_view_paginator(Changelog, page_number)

    return render(request, 'changelog.html', {'title': title,
                                              'show_page': not page_url,
                                              'changelogs': changelogs})
