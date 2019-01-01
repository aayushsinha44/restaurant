from django.http import HttpResponse, HttpResponseBadRequest
from user.helper.decorator import login_required
from menu.models import Item
from user.helper.constants import HTTP_SUCCESS, HTTP_UNAUTHORIZED, HTTP_NOT_ACCEPTABLE
from django.views.decorators.csrf import csrf_exempt
from menu.helper import ItemObject
import json

@csrf_exempt
@login_required
def item(request, id):
    itemObject = ItemObject(id)
    if itemObject.isValid() == True:
        return HttpResponse(json.dumps({"success": True,
                                        "code": HTTP_SUCCESS,
                                        "data": itemObject.getItem()}), content_type='application/json')
    else:
        return HttpResponseBadRequest(json.dumps({"success": False,
                                                "code": HTTP_NOT_ACCEPTABLE,
                                                "message": "invalid id"}), content_type='application/json')


