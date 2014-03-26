from django.test import TestCase
from core.models import WikiPage


class WikiPageTest(TestCase):

    def test_title(self):
        """Testing that a wiki page title is generated correctly from its url
            value.
        """

        page = WikiPage.objects.create(url='Dummy_TestPage/For/Fairfax')

        # Testing that Wikipage.title property converts a CamelCase properly.
        page.url = 'HumanBody'
        self.assertEqual('Human Body', page.title)

        # Testing that Wikipage.title property converts a underscore properly.
        page.url = 'human_body'
        self.assertEqual('Human Body', page.title)

        # Testing that Wikipage.title property converts a CamelCase/underscore
        # properly.
        page.url = 'Parts_of_the_HumanBody'
        self.assertEqual('Parts Of The Human Body', page.title)

        # Testing that Wikipage.title property converts a CamelCase/slash
        # properly.
        page.url = 'HumanBody/Parts'
        self.assertEqual('Human Body / Parts', page.title)


