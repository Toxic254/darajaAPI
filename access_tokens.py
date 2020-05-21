import requests
from requests.auth import HTTPBasicAuth

import keys


def generate_access_token():
    #Generating My Access Token 
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    json_response = r.json()

    #Accessing the Header JSON element from the Dictionary 
    my_access_token = json_response['access_token']

    return my_access_token

generate_access_token()