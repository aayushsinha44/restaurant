from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from user.helper.google_auth import evaluate_google_token, get_value_from_token
from user.helper.token import create_token
from user.models import User
import json
from user.helper.constants import HTTP_NOT_ACCEPTABLE, VALID_GOOGLE_TOKEN, \
            INVALID_GOOGLE_TOKEN, GOOGLE_VALUE_ERROR, HTTP_INTERNAL_SERVER_ERROR, HTTP_SUCCESS, HTTP_UNAUTHORIZED
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    try:        
        token = request.POST["token"]
        token_status = evaluate_google_token(token)
        if token_status == VALID_GOOGLE_TOKEN:
            google_values = get_value_from_token(token)
            email = google_values["email"]
            name = google_values["name"]

            if User.objects.filter(email=email).count() == 0:
                # New User
                User.objects.create(email=email, name=name)
                user_token=create_token(email)
                return HttpResponse(json.dumps({"success": True,
                                                "code": HTTP_SUCCESS,
                                                "token": user_token}), content_type='application/json')
            else:
                # Existing User
                email = list(User.objects.filter(email=email).values())[0]["email"]
                user_token=create_token(email)
                return HttpResponse(json.dumps({"success": True,
                                                "code": HTTP_SUCCESS,
                                                "token": user_token}), content_type='application/json')
        elif token_status == INVALID_GOOGLE_TOKEN:
            return HttpResponseBadRequest(json.dumps({"success": False,
                                        "code": HTTP_NOT_ACCEPTABLE,
                                        "message": "invalid google token"}), content_type='application/json')
        elif token_status == GOOGLE_VALUE_ERROR:
            return HttpResponseServerError(json.dumps({"success": False,
                                        "code": HTTP_INTERNAL_SERVER_ERROR,
                                        "message": "something went wrong"}), content_type='application/json')

    except:
        return HttpResponseBadRequest(json.dumps({"success": False,
                                        "code": HTTP_NOT_ACCEPTABLE,
                                        "message": "token not set"}), content_type='application/json')