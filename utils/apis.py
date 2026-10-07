import requests

class APIS:

    BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

    def __init__(self):
        self.headers = {
            'Accept': 'text/plain',
            'Content-Type': 'application/json'
        }

    def get_all_activities(self):
        return requests.get(f"{self.BASE_URL}", headers=self.headers)

    def get_activity_by_id(self, activity_id):
        return requests.get(f"{self.BASE_URL}/{activity_id}", headers=self.headers)

    def post_activity(self, body):
        return requests.post(f"{self.BASE_URL}", headers=self.headers, json=body)

    def put_activity(self, activity_id, body):
        return requests.put(f"{self.BASE_URL}/{activity_id}", headers=self.headers, json=body)

    def delete_activity(self, activity_id):
        return requests.delete(f"{self.BASE_URL}/{activity_id}", headers=self.headers)
