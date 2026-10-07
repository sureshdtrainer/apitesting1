import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')

print(response.status_code)
print('---Response Header----\n')
print(response.headers)
print('---Response Body----\n')
print(response.json())

#Validation/Assertions here
assert response.status_code==200
