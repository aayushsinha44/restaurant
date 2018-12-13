GOOGLE_CLIENT_ID = "806644253179-mrd07ge79hv48ljt7np6alcftlhhta8n.apps.googleusercontent.com"

TOKEN_EXPIRY_DAYS=30 # 30 days

INVALID_GOOGLE_TOKEN=1001
VALID_GOOGLE_TOKEN=2001
TOKEN_EXPIRED=1002
INVALID_TOKEN=1003
VALID_TOKEN=2002

GOOGLE_VALUE_ERROR=3001

HTTP_SUCCESS=200
HTTP_UNAUTHORIZED=401
HTTP_NOT_ACCEPTABLE=406
HTTP_INTERNAL_SERVER_ERROR=501

import random
import string

SECRET_KEY=None

def get_secret_key():
    global SECRET_KEY
    if SECRET_KEY == None:
        SECRET_KEY = generate_secret_key()
        return SECRET_KEY
    else:
        return SECRET_KEY

def generate_secret_key():
    secret_key = []
    for i in range(64):
        flag = random.randint(0,1)
        if flag==0:
            secret_key.append(random.choice(string.digits))
        elif flag == 1:
            secret_key.append(random.choice(string.ascii_letters))
        else:
            secret_key.append(random.choice(string.punctuation))
    return "".join(secret_key)