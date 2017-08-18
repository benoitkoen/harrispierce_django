import pytest
from django.test import TestCase, client
from django.http import HttpRequest
from django.template.loader import render_to_string
from mock import NonCallableMock, patch

from harrispierce.factories import JournalFactory, SectionFactory
from harrispierce.views import IndexView

@pytest.mark.django_db
class TestIndex(TestCase):
    maxDiff = None

    @classmethod
    def setUpTestData(cls):
        cls.myclient = client.Client()

    def test_index_view(self):
        response = self.myclient.get('/')
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'harrispierce/index.html')

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        IndexViewInstance = IndexView()
        response = IndexViewInstance.get(request)
        expected_html = render_to_string('harrispierce/index.html')
        self.assertMultiLineEqual(response.content.decode(), expected_html)

    #def test_index_content(self):
    #    response = self.myclient.get('/', {'journals': })
    #    self.assertContains(response, "Invalid message here", 1, 200)


