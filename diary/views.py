# coding:UTF-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist
from own.models import DiaryModel
from own.lib import upload_file, get_download_file_url
import time
import hashlib
import os
import json


def index(request):
    "日记主界面"
    return render_to_response("diary/index.html")

def write(request):
    "写日记"
    if request.method == "GET":
        return render_to_response("diary/write.html")
    else:
        if 'pic' in request.FILES:
            pic_data = request.FILES['pic'].read()
            path = hashlib.md5(pic_data).hexdigest()
            if not upload_file(path, pic_data):
                return HttpResponseServerError("上传文件出错!")
            pic_url = path
            """
            pic_url = os.path.join('/static/upload/pic/', path[0:8], path[8:16], path[16:24], path[24:32] + ".png")

            #保存上传的图片
            fp_path = pic_url[1:]
            if not os.path.exists(fp_path):
                dir_path = os.path.dirname(fp_path)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                open(fp_path, 'wb').write(pic_data)
            """

        else:
            pic_url = ''
        content = request.POST.get('content', None).replace("\n","<br>")
        dao = DiaryModel(uid=request.session['user'], picUrl=pic_url, content=content, status=0, pushTime=time.strftime("%Y-%m-%d %H:%M:%S"))
        dao.save()
        return HttpResponseRedirect("/diary/")


def get_message(request):
    if request.method == "POST":
        year = time.strftime("%Y年")
        month = time.strftime("%m月")

        page = int(request.POST.get('page', 1)) - 1
        offer = 10
        start_number = page * offer
        objs = DiaryModel.objects.order_by("-id").filter(uid=request.session['user'], status=0,)[start_number:(start_number + offer)]
        r = []
        for obj in objs:
            data = dict()
            data['id'] = obj.id
            data['content'] = obj.content
            data['time'] = obj.pushTime.strftime("%Y年%m月%d日").replace(year, "").replace(month, "")
            r.append(data)

        response = HttpResponse(json.dumps(r))
        response['Content-Type'] = "application/json"
        return response
    else:
        return HttpResponseNotFound("页面被程序猴子吃了！")


def log(request, diary_id):
    "具体日记"

    try:
        obj = DiaryModel.objects.get(id=diary_id, uid=request.session['user'], status=0)
        if obj.picUrl:
            obj.picUrl = get_download_file_url(obj.picUrl)
        return render_to_response("diary/log.html", {'obj': obj})
    except ObjectDoesNotExist:
        return HttpResponseForbidden("不要查看别人的日记")


def delete(request, diary_id):
    "删除日记"
    DiaryModel.objects.filter(uid=request.session['user'], id=diary_id).update(status=1)
    return HttpResponseRedirect("/diary/")

