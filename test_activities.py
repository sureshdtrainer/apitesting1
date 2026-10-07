import pytest
import requests

def test_get_activity_by_id():
    response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/10')
    assert response.status_code == 200
    assert response.json()['id'] == 10