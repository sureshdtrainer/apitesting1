import pytest
from utils.apis import APIS

@pytest.fixture(scope="module")
def apis():
    return APIS()


def test_get_all_activities(apis):
    #api = APIS()
    response = apis.get_all_activities()
    print(response.status_code)
    print(response.json())
    print(response.headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_activity_by_id(apis):
    #api = APIS()
    activity_id = 5  # Replace with a valid activity ID
    response = apis.get_activity_by_id(activity_id)
    print(response.status_code)
    print(response.json())
    print(response.headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json().get("id") == activity_id

def test_post_activity(apis):
    #api = APIS()
    body = {
        "id": 150,
        "title": "New Activity",
        "dueDate": "2024-06-01T00:00:00Z",
        "completed": False
    }
    response = apis.post_activity(body)
    print(response.status_code)
    print(response.json())
    print(response.headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json().get("title") == body["title"]

# This is the test case for Update Activity API Success


def test_update_activity(apis, load_test_data):

    # request_body = {
    #    "id": 50,
    #    "title": "Updated Learning API Testing",
    #    "dueDate": "2025-09-24T07:22:03.17Z",
    #    "completed": True
    # }
    request_body = load_test_data["update_activity"]
    response = apis.put_activity(50, request_body)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['id'] == 50
    assert response.json()['title'] == "Updated Task"

# This is the test case for Delete Update Activity API Success


def test_delete_activity(apis):
    response = apis.delete_activity(50)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200
    assert response.text == ""

