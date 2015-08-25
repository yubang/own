# coding:UTF-8


from django.conf.urls import url, patterns


urlpatterns = patterns('paper.views',
    url(r'^$', 'index'),
    url(r'^data$', 'data'),
)
