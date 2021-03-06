from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^index.we$', views.index),
    url(r'^tv.we$', views.tv, name='tv'),
    url(r'^voice_of_china_2014.we$', views.voice_of_china_2014, name='voice_of_china_2014'),
    url(r'^worldcup_2014.we$', views.worldcup_2014, name='worldcup_2014'),
)
