from django.urls import re_path
from menu.views.item import item
urlpatterns = [
    re_path(r'^item/<int:id>/$', item, name = 'item')
]