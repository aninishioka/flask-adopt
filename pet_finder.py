import requests
import random
import os
from dotenv import load_dotenv

env = load_dotenv()

PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']
PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']

def update_auth_token_string():
    resp =  requests.post(
    "https://api.petfinder.com/v2/oauth2/token",
    data={"grant_type" : "client_credentials",
          "client_id" : f"{PETFINDER_API_KEY}",
          "client_secret" : f"{PETFINDER_SECRET_KEY}"}
    )
    return resp.json()['access_token']

token = update_auth_token_string()


def get_pet(token):
    pets = requests.get("https://api.petfinder.com/v2/animals",
        params={"limit": "100"},
        headers={"Authorization": f"Bearer {token}"}
        ).json()
    random_pet = random.choice(pets['animals'])
    name = random_pet['name']
    age = random_pet['age']
    photo_data = random_pet['photos'][0] if random_pet['photos'] else {}
    photo_url = photo_data['medium'] if photo_data else ''

    return {'name': name, 'age': age, 'photo_url': photo_url}




