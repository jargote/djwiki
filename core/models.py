from django.db import models
from django.contrib.auth.models import User


class WikiPage(models.Model):
    """This class models a Wiki Page.

    Attributes:
        url: String representing the WikiPage's instance url.
        title: String representing the wiki page's title.
        body: Text to format as Html using Markdown.
        author: User who's created the WikiPage model instance.
        created_on: Datetime timestamp that represents when a page instance was
            created.
        updated_on: Datetime timestamp that represent when a page instance was
            last updated.
    """

    url = models.CharField('Url', max_length=150)
    title = models.CharField('Title', max_length=150)
    body = models.TextField('Body', blank=True)
    author = models.ForeignKey(User, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_on',)


class Changelog(models.Model):
    """This model class represents a change log for one edit operation on a
    WikiPage instance.

    Attributes:
        comment: Text containing comments describing the change made
            to the referenced WikiPage instance.
        page: ForeignKey to the WikiPage instance that has been changed.
        author: ForeignKey to the User instance that modified the referenced
            WikiPage
        created_on: Datetime timestamp that represents when a ChangeLog instance
            was made.
    """

    comments = models.TextField('Comments')
    page = models.ForeignKey(WikiPage)
    author = models.ForeignKey(User, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_on',)