import requests
from requests.auth import HTTPBasicAuth

from access_tokens import generate_access_token
from keys import short_code
from keys import test_msisdn 

# This code runs offline and is client initiated. We need 2 URL's.

def register_url():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": short_code,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://uzuri.com",
        "ValidationURL": "https://uzuri.com"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

# No need to run this we have already registered our mock URL
register_url()


def simulate_c2b_transaction():

    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": short_code,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "1",
        "Msisdn": test_msisdn,
        "BillRefNumber": "12345678"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

simulate_c2b_transaction()
