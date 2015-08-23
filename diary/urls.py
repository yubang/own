# coding:UTF-8

from django.conf.urls import url, patterns


urlpatterns = patterns('diary.views',
    url(r'^$', 'index'),
    url(r'^write$', 'write'),
    url(r'^getMessage$', 'get_message'),
    url(r'^log/(?P<diary_id>\d+)$', 'log'),
    url(r'^delete/(?P<diary_id>\d+)$', 'delete'),
)