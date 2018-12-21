from django.http import HttpResponse, HttpResponseBadRequest
import json
from user.models import Address, User
from django.views.decorators.csrf import csrf_exempt
from user.helper.decorator import login_required
from user.helper.constants import HTTP_NOT_ACCEPTABLE, VALID_GOOGLE_TOKEN, \
            INVALID_GOOGLE_TOKEN, GOOGLE_VALUE_ERROR, HTTP_INTERNAL_SERVER_ERROR, HTTP_SUCCESS, HTTP_UNAUTHORIZED
from user.helper.token import get_email

@csrf_exempt
@login_required
def address(request):
    if request.method == 'POST':
        try:
            email = get_email(request)
            address=request.POST["address"]
            city=request.POST["city"]
            state=request.POST["state"]
            country=request.POST["country"]
            pincode=request.POST["pincode"]
            phone_number=request.POST["phone_number"]

            user_object = User.objects.get(email=email)

            Address.objects.create(email=user_object,
                                    address=address,
                                    city=city,
                                    state=state,
                                    country=country,
                                    pincode=pincode,
                                    phone_number=phone_number)

            return HttpResponse(json.dumps({"success": True,
                                            "code": HTTP_SUCCESS,
                                            "messsage": "address added successfully"}), content_type='application/json')
                        
        except:
            return HttpResponseBadRequest(json.dumps({"success": False,
                                                "code": HTTP_NOT_ACCEPTABLE,
                                                "message": "data not set"}), content_type='application/json')

    elif request.method == 'GET':
        email = get_email(request)

        user_object = User.objects.get(email=email)

        address_list = list(Address.objects.filter(email=user_object).values())

        return HttpResponse(json.dumps({"success": True,
                                        "code": HTTP_SUCCESS,
                                        "address": address_list}), content_type='application/json')        

    else:
        return HttpResponseBadRequest(json.dumps({"success": False,
                                                "code": HTTP_NOT_ACCEPTABLE,
                                                "message": "Unsupported Method"}), content_type='application/json')