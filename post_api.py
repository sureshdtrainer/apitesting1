import requests

# Example of a POST request with custom headers
request_headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json',
}

reqest_body = {
    "id": 50,
    "title": "string",
    "dueDate": "2023-10-05T14:48:00.000Z",
    "completed": True,
}

response = requests.post(
    'https://fakerestapi.azurewebsites.net/api/v1/Activities', headers=request_headers, json=reqest_body)

print(response.status_code)
print(response.json())
print(response.headers)

assert response.status_code == 200

response_body = response.json()
print(response_body['id'])

assert response.status_code == 200
assert response_body['id'] == 50
