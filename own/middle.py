# coding:UTF-8

from django.http import HttpResponseRedirect
import re


class LoginCheck(object):
    "检查权限"
    def __init__(self):
        pass

    def process_request(self, request):
        if 'user' not in request.session:
            if request.path != '/' and not re.search(r'^/account/', request.path):
                return HttpResponseRedirect("/")