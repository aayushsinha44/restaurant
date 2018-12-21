from django.http import HttpResponse, HttpResponseBadRequest
from user.helper.decorator import login_required
from django.views.decorators.csrf import csrf_exempt
from user.helper.token import get_email
import json
from user.models import User
from user.helper.constants import HTTP_NOT_ACCEPTABLE, VALID_GOOGLE_TOKEN, \
            INVALID_GOOGLE_TOKEN, GOOGLE_VALUE_ERROR, HTTP_INTERNAL_SERVER_ERROR, HTTP_SUCCESS, HTTP_UNAUTHORIZED

@csrf_exempt
@login_required
def profile(request):
    if request.method == 'GET':
        email = get_email(request)
        user_profile = list(User.objects.filter(email=email).values())[0]
        name = user_profile["name"]
        phone_number = user_profile["phone_number"]
        picture_url = user_profile["picture_url"]

        return HttpResponse(json.dumps({"success": True,
                                        "code": HTTP_SUCCESS,
                                        "name": name,
                                        "email": email,
                                        "picture": picture_url,
                                        "phone_number": phone_number}), content_type='application/json')

    elif request.method == 'POST':
        try:
            email = get_email(request)
            name = request.POST["name"]
            phone_number = request.POST["phone_number"]

            user_object = User.objects.get(email=email)
            user_object.name = name
            user_object.phone_number = phone_number
            user_object.save()

            return HttpResponse(json.dumps({"success": True,
                                        "code": HTTP_SUCCESS,
                                        "message": "Profile updated successfully"}), content_type='application/json')


        except:
            return HttpResponseBadRequest(json.dumps({"success": False,
                                                "code": HTTP_NOT_ACCEPTABLE,
                                                "message": "Data not set"}), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({"success": False,
                                                "code": HTTP_NOT_ACCEPTABLE,
                                                "message": "Unsupported Method"}), content_type='application/json')


@csrf_exempt
@login_required
def add_phone(request):
    try:
        phone_number=request.POST["phone_number"]
        email = get_email(request)
        
        user_object = User.objects.get(email=email)
        user_object.phone_number = phone_number
        user_object.save()

        return HttpResponse(json.dumps({"success": True,
                                        "code": HTTP_SUCCESS,
                                        "message": "Phone number updated"}), content_type='application/json')
        

    except:
        return HttpResponseBadRequest(json.dumps({"success": False,
                                                "code": HTTP_UNAUTHORIZED,
                                                "message":"phone number not set"}), content_type='application/json')

