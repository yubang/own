# coding:UTF-8

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from own.models import TimeBottleModel
import time
import datetime


def index(request):
    return render_to_response("timeBottle/index.html")


def get(request):
    objs = TimeBottleModel.objects.order_by("-id").filter(uid=request.session['user'], targetTime=datetime.date.today())
    if not objs:
        return HttpResponse("")

    r = list()
    for obj in objs:
        data = dict()
        data['content'] = obj.content
        data['createTime'] = obj.createTime.strftime("%Y年%m月%d日 %H时%M分%S秒")

        temp_obj = datetime.datetime.now() - obj.createTime
        days = temp_obj.days
        if days == 0:
            data['time'] = "今天"
        elif days == 1:
            data['time'] = "昨天"
        elif days == 2:
            data['time'] = "前天"
        else:
            data['time'] = str(days) + "天前"

        r.append(data)

    return render_to_response("timeBottle/get.html", {'objs' : r})


def make(request):
    "制作瓶子"
    if request.method == "GET":
        return render_to_response("timeBottle/make.html")
    else:
        content = request.POST.get('content', None)
        target_time = request.POST.get('targetTime', None)
        obj = TimeBottleModel(content=content, targetTime=target_time, createTime=time.strftime("%Y-%m-%d %H:%M:%S"), status=0, uid=request.session['user'])
        obj.save()
        return HttpResponseRedirect("/time/")
