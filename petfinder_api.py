import requests
from app import PETFINDER_SECRET_KEY, PETFINDER_API_KEY

def update_auth_token_string():
    return requests.post(
    "https://api.petfinder.com/v2/oauth2/token",
    data={"grant_type" : "client_credentials",
          "client_id" : f"{PETFINDER_API_KEY}",
          "client_secret" : f"{PETFINDER_SECRET_KEY}"}
)
def get_pets(token):
    return requests.get("https://api.petfinder.com/v2/animals",
        params={"limit": "100"},
        headers={"Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4TVNNWVF4QXhaY1FFRlR1c0NmWUdJOTY4dWloZU9KVURBeURCTDhDcDFpUHF4T0NvRiIsImp0aSI6IjJhZDg0MGYzMTIwZGVhYzAzODgyOWNlNTk5M2Q5ZDAwYzE3ODQ1NzgwM2JiNDc0NDEwZTRiZjZhNWI5NzQ5N2Q4NDYzMmU1Nzg0MmIxMzJlIiwiaWF0IjoxNzA5MzM3MzQ2LCJuYmYiOjE3MDkzMzczNDYsImV4cCI6MTcwOTM0MDk0Niwic3ViIjoiIiwic2NvcGVzIjpbXX0.NnX_gu7YEnWaZ3cM0oJpskHgzRjBHasHc3M78PwHNd773wzwl6YsxDUxnJ4Dtye2S9VhBOqLANKkh7R807cZaVnCjD8nDagNwRDOEUbKcvgrdkIYk0gHo92QfI-p8f96dAEFHsHK7JY3kGqvUkb5W50j8J-YZtXnbmlsFCp5Cmr5ID30o_xe-HBiOskWwet8U-VyZtJFr68Rkr_Sp-8LqE4dbjcF1OfjjFUwPQK366IHNJLDIia7vW438DSufc3TKSM44MiXGvmPO9Cs6IwDYWPQ9j1Iqx8KoHDBfHDPuZe0fyw1io-XXbZTE9bFZ8yYYKHQ9sHDYqKuAVuFvkdVuQ"}
        )




