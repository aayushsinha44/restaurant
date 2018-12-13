from datetime import date, datetime
from hashlib import sha256
from user.helper.constants import TOKEN_EXPIRY_DAYS, VALID_TOKEN, INVALID_TOKEN, TOKEN_EXPIRED, get_secret_key
import jwt

def calcuate_day_difference(date):
    delta=date.today()-date
    return int(delta.days)

def check_token(token):
    try:
        jwt_string = jwt.decode(token, get_secret_key(), algorithms=['HS256'])
        # email = jwt_string["email"]
        date_login = jwt_string["date"]
        date_login = datetime.strptime(date_login, '%Y-%m-%d').date()
        diff = calcuate_day_difference(date_login)
        if diff <= TOKEN_EXPIRY_DAYS:
            return VALID_TOKEN
        else:
            return TOKEN_EXPIRED
    except:
        return INVALID_TOKEN

def create_token(email):
    token = jwt.encode({'email': email, 'date': str(date.today())}, get_secret_key(), algorithm='HS256')
    token = token.decode()
    return token

def get_email(request):
    try:
        token = request.META['HTTP_TOKEN']
        jwt_string = jwt.decode(token, get_secret_key(), algorithms=['HS256'])
        email = jwt_string["email"]
        return email
    except:
        return INVALID_TOKEN





