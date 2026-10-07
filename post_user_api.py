import requests

#PArt 1: Create a user using POST request
# Example of a POST with Authorization Bearer request with custom headers
request_headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 0b5b0eac4854cb5fdd8048c8406cb60fc8476e30dee6d2fb8a64a7ad7e86749e'
}

reqest_body = {
    "name": "Prof. Atreyee Naik",
    "email": "naik_prof_atreyee111555@zulauf.test",
    "gender": "male",
    "status": "inactive"
}

response = requests.post(
    'https://gorest.co.in/public/v2/users', headers=request_headers, json=reqest_body)

print(response.status_code)
print(response.json())
print(response.headers)

response_body = response.json()
print(response_body['id'])

assert response.status_code == 201

#Part 2: Get the user by id using GET request
#Get the user by id

get_response = requests.get(
    f'https://gorest.co.in/public/v2/users/{response_body["id"]}', headers=request_headers)

print(get_response.status_code)
print(get_response.json())

assert get_response.status_code == 200
assert get_response.json()['id'] == response_body['id']
