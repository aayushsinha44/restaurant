from django.test import TestCase
from user.helper.token import create_token, check_token
from user.helper.constants import TOKEN_EXPIRY_DAYS, VALID_TOKEN, INVALID_TOKEN, TOKEN_EXPIRED, get_secret_key
import jwt

# Create your tests here.
class TokenCreationAndValidationTest(TestCase):
    def setUp(self):
        self.email = "a@test1.com"
        self.token = create_token(self.email)
        self.expired_token = jwt.encode({'email': self.email, 'date': '2011-01-01'}, get_secret_key(), algorithm='HS256').decode()

    def test_token(self):
        status = check_token(self.token)
        self.assertEqual(status, VALID_TOKEN)
        
    def test_expired_token(self):
        status = check_token(self.expired_token)
        self.assertEqual(status, TOKEN_EXPIRED)

class SecretKeyGenrationTest(TestCase):
    def setUp(self):
        self.secret_key = get_secret_key()

    def test_secret_key(self):
        self.assertEqual(self.secret_key, get_secret_key())