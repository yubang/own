# coding:UTF-8


from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):
    return render_to_response("paper/index.html")


def data(request):
    "获取纸条"
    return HttpResponse("123")