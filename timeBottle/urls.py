# coding:UTF-8

from django.conf.urls import url, patterns


urlpatterns = patterns('timeBottle.views',
    url(r'^$', 'index'),
    url(r'^get$', 'get'),
    url(r'^make$', 'make'),
)
