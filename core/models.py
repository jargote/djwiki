import re
import markdown

from django.db import models
from django.contrib.auth.models import User


class WikiPage(models.Model):
    """This class models a Wiki Page.

    Attributes:
        url: String representing the WikiPage's instance url.
        markdown: File path to the WikiPage markdown file.
        author: User who's created the WikiPage model instance.
        created_on: Datetime timestamp that represents when a page instance was
            created.
        updated_on: Datetime timestamp that represent when a page instance was
            last updated.
    """

    url = models.CharField('Url', max_length=150)
    markdown = models.FilePathField()
    author = models.ForeignKey(User, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_on',)

    @property
    def title(self):
        """This method returns the wiki page title from the page url.

        1. Underscores should be converted into spaces.
        2. Capital letters surrounded by lowercase letters should have a space
            added before them.
        3. Slashes should have spaces added around them.
        """

        title = re.sub("([a-z])([A-Z])","\g<1> \g<2>", self.url)
        title = title.replace('_', ' ').replace('/', ' / ')
        return title.title()

    @property
    def rendered_html(self):
        file = open(self.markdown, 'rb')
        content = ''.join(file.readlines())
        file.close()

        return markdown.markdown(content)



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
    wikipage = models.ForeignKey(WikiPage)
    author = models.ForeignKey(User, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_on',)

    @property
    def created_by(self):
        """Gets Changelog author's username.

        Returns:
            String representing change log author's username.
        """

        if not self.author:
            return 'Anonymous'

        return self.author.username