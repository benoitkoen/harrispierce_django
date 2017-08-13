import pytest
from django.test import TestCase, client
from harrispierce.factories import JournalFactory, SectionFactory

@pytest.mark.django_db
class TestIndex(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.myclient = client.Client()

    def test_index_view(self):
        response = self.myclient.get('/')
        assert response.status_code == 200

    def test_index_content(self):
        section0 = SectionFactory()
        section1 = SectionFactory()
        section2 = SectionFactory()
        print('wijhdjk: ', section0)
        journal1 = JournalFactory.create(sections=(section0, section1, section2))

        response = self.myclient.get('/')

        print('wijhdjk: ', journal1)
        self.assertEquals(journal1.name, 'Section0')
        self.assertContains(response, journal1.name)

