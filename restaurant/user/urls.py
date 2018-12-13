from django.urls import re_path
from user.views.login import login
from user.views.profile import add_phone
urlpatterns = [
    re_path(r'^login/$', login, name = 'login'),
    re_path(r'^add_phone/$', add_phone,name='add_phone')
]