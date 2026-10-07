import requests

# DELETE Activity by id
response = requests.delete(
    'https://fakerestapi.azurewebsites.net/api/v1/Activities/10')

print(response.status_code)
print(response.headers)

assert response.status_code == 200
