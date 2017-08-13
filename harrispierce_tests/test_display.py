import pytest

@pytest.mark.django_db
class TestDisplay:

    def test_display_view(self, client):
        response = client.get('/display.html/')
        assert response.status_code == 200