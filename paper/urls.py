# coding:UTF-8


from django.conf.urls import url, patterns


urlpatterns = patterns('paper.views',
    url(r'^$', 'index'),
    url(r'^data$', 'data'),
    url(r'^write$', 'write'),
    url(r'^delete/(?P<paper_id>\d+)$', 'delete'),
)
