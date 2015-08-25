# coding:UTF-8


from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from own.models import PaperModel
import json
import random
import datetime


def index(request):
    return render_to_response("paper/index.html")


def data(request):
    """获取纸条"""
    paper_number = PaperModel.objects.filter(uid=request.session['user'], status=0).count()

    if paper_number == 0:
        response = HttpResponse(json.dumps({'id': 0, 'data': "你还没有字条呢！"}))
    else:
        index = random.randint(0, paper_number-1)
        papers = PaperModel.objects.filter(uid=request.session['user'], status=0)[index:index+1]
        paper = papers[0]
        response = HttpResponse(json.dumps({'id': paper.id, 'data': paper.content}))

    response['Content-Type'] = 'application/json'
    return response


def write(request):
    """写小纸条"""
    if request.method == "GET":
        return render_to_response("paper/write.html")
    else:
        content = request.POST.get('content', None)
        paper = PaperModel(uid=request.session['user'], status=0, content=content, createTime=datetime.datetime.now())
        paper.save()
        return HttpResponseRedirect("/paper/")


def delete(request, paper_id):
    """删除小纸条"""
    PaperModel.objects.filter(uid=request.session['user'], id=paper_id).update(status=1)
    return HttpResponseRedirect("/paper/")