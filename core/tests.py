from django.test import TestCase
from django.contrib.auth.models import User

from core.models import WikiPage, Changelog



class WikiPageTest(TestCase):
    """Tests suite for WikiPage model class."""

    def setUp(self):
        # Creating a test markdown file.
        self.markdown_text = u'\n'.join([
            u'A First Level Header',
            u'====================',
            u'A Second Level Header',
            u'---------------------',
            u'Now is the time for all good men to come to the aid of',
            u'their country. This is just a regular paragraph.\n',
            u'The quick brown fox jumped over the lazy dog\'s back.'])

    def test_title(self):
        """Tests that a wiki page title is generated correctly from its url
            value.
        """

        wikipage = WikiPage()

        # Testing that Wikipage.title property converts a CamelCase properly.
        wikipage.url = 'HumanBody'
        self.assertEqual('Human Body', wikipage.title)

        # Testing that Wikipage.title property converts a underscore properly.
        wikipage.url = 'human_body'
        self.assertEqual('Human Body', wikipage.title)

        # Testing that Wikipage.title property converts a CamelCase/underscore
        # properly.
        wikipage.url = 'Parts_of_the_HumanBody'
        self.assertEqual('Parts Of The Human Body', wikipage.title)

        # Testing that Wikipage.title property converts a CamelCase/slash
        # properly.
        wikipage.url = 'HumanBody/Parts'
        self.assertEqual('Human Body / Parts', wikipage.title)

    def test_render_html(self):
        """Tests that Wiki.render_html property returns rendered HTML from the
        markdown file associated to the WikiPage instance.
        """

        # Linking markdown file to WikiPage instance.
        wikipage = WikiPage(url='DummyWikiPageUrl', body=self.markdown_text)

        # Testing that Markdown renders HTML correctly.
        self.assertEqual(
            u'<h1>A First Level Header</h1>\n'
            u'<h2>A Second Level Header</h2>\n'
            u'<p>Now is the time for all good men to come to the aid of\n'
            u'their country. This is just a regular paragraph.</p>\n'
            u'<p>The quick brown fox jumped over the lazy dog\'s back.</p>',
            wikipage.rendered_html)


class ChangelogTest(TestCase):
    """Tests suite for Changelog model class."""

    def setUp(self):
        self.test_wikipage = WikiPage.objects.create(url='TestWikiPage')

    def test_created_by(self):
        """Tests that Changelog author username is returned correctly."""

        # Creating a dummy User object - Dummy author.
        dummy_author = User.objects.create(username='DummyAuthor',
                                           email='dummy@djwiki.com')

        # Creating a test Changelog instance.
        changelog = Changelog.objects.create(comments='This is my first change',
                                             wikipage=self.test_wikipage,
                                             author=dummy_author)

        # Testing that author username is returned correctly.
        self.assertEqual('DummyAuthor', changelog.created_by)

        # Setting Changelog author to None.
        changelog.author = None

        # Testing that author username is 'Anonymous'.
        self.assertEqual('Anonymous', changelog.created_by)
