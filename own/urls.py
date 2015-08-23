from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'own.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'own.views.index'),
    url(r'^account/(?P<option>.+)$', 'own.views.account'),
    url(r'^own/$', 'own.views.own'),
    url(r'^own/exit$', 'own.views.exit_account'),
    url(r'^diary/', include("diary.urls")),
)
