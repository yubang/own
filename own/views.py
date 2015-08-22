# coding:UTF-8


from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from own.models import AccountModel
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
import hashlib
import json
import time


def index(request):
    "主界面"
    return render_to_response("index.html")


def account(request, option):
    "账号登录或注册"

    if 'user' in request.session:
        return HttpResponseRedirect("/own/")

    if request.method == 'GET':
        return render_to_response("base/account.html", {"option" : option,})
    else:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if option == "login":
            try:
                obj = AccountModel.objects.get(username=username)
                if hashlib.md5(password + obj.halt).hexdigest() == obj.password:
                    obj.loginTime = time.strftime("%Y-%m-%d %H:%M:%S")
                    obj.save()
                    request.session['user'] = time.time()
                    code = 0
                else:
                    code = -2
            except ObjectDoesNotExist:
                code = -1
        else:
            try:
                halt = hashlib.md5(str(time.time())).hexdigest()
                password = hashlib.md5(password + halt).hexdigest()
                obj = AccountModel(username=username, password=password, halt=halt, registerTime=time.strftime("%Y-%m-%d %H:%M:%S"))
                obj.save()
                request.session['user'] = time.time()
                code = 0
            except IntegrityError:
                code = -1
        response = HttpResponse(json.dumps({'code': code}))
        response['Content-Type'] = "application/json"
        return response


def own(request):
    "菜单"
    return render_to_response("base/own.html")

def exit_account(request):
    "退出登录"
    if 'user' in request.session:
        del request.session['user']
    return HttpResponseRedirect("/")