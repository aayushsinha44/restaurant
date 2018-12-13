from django.http import HttpResponse, HttpResponseBadRequest
from user.helper.decorator import login_required
from django.views.decorators.csrf import csrf_exempt
from user.helper.token import get_email
import json
from user.helper.constants import HTTP_NOT_ACCEPTABLE, VALID_GOOGLE_TOKEN, \
            INVALID_GOOGLE_TOKEN, GOOGLE_VALUE_ERROR, HTTP_INTERNAL_SERVER_ERROR, HTTP_SUCCESS, HTTP_UNAUTHORIZED

@csrf_exempt
@login_required
def profile(request):
    pass


@csrf_exempt
@login_required
def add_phone(request):
    try:
        phone_number=request.POST["phone_number"]
        email = get_email(request)
        

    except:
        return HttpResponseBadRequest(json.dumps({"success": False,
                                                "code": HTTP_UNAUTHORIZED,
                                                "message":"phone number not set"}), content_type='application/json')

