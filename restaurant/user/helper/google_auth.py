from google.oauth2 import id_token
from google.auth.transport import requests

from user.helper.constants import INVALID_GOOGLE_TOKEN, VALID_GOOGLE_TOKEN, GOOGLE_VALUE_ERROR, GOOGLE_CLIENT_ID

def evaluate_google_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return INVALID_GOOGLE_TOKEN

        return VALID_GOOGLE_TOKEN

    except ValueError:
        return GOOGLE_VALUE_ERROR

def get_value_from_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return INVALID_GOOGLE_TOKEN

        email = idinfo['email']
        name = idinfo['name']
        picture = idinfo['picture']
        return {"email" :email, "name": name, "picture": picture}
        
    except ValueError:
        return GOOGLE_VALUE_ERROR