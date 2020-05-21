import requests
from requests.auth import HTTPBasicAuth

from access_tokens import generate_access_token
from encode import generate_password
from utils import generate_timestamps
import keys


#Starting Lipa Na Mpesa process
def lipa_na_mpesa():
  access_token = generate_access_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = {
    "BusinessShortCode": keys.business_short_code,
    "Password": generate_password(),
    "Timestamp": generate_timestamps(),
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "100",
    "PartyA": keys.phone_number,
    "PartyB": keys.business_short_code,
    "PhoneNumber": keys.phone_number,
    "CallBackURL": "https://uzuri.com",
    "AccountReference": "0736745458",
    "TransactionDesc": "This is an API Test Transaction"
  }

  response = requests.post(api_url, json=request, headers=headers)
  print(response.text)

lipa_na_mpesa()
