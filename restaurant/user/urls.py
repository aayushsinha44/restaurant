from django.urls import re_path
from user.views.login import login
from user.views.profile import add_phone, profile
from user.views.address import address
urlpatterns = [
    re_path(r'^login/$', login, name = 'login'),
    re_path(r'^add_phone/$', add_phone,name='add_phone'),
    re_path(r'^profile/$', profile, name='profile'),
    re_path(r'^address/$', address, name='address')
]