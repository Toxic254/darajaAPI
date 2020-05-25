import base64
from datetime import datetime

import keys
import utils

def generate_password():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    data_to_encode = keys.business_short_code + keys.lipa_na_mpesa_passkey + formatted_time
    # We have to convert the object to bytes first
    # Data to be encoded back to String
    encoded_string = base64.b64encode(data_to_encode.encode())
    # Decoding wierd object to String format
    decoded_password = encoded_string.decode('utf-8')

    return decoded_password

generate_password()
