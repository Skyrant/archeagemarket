from django.conf.urls import patterns, url, include
from workorder import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^find_profession/$', views.find_profession, name='find_profession'),
                       url(r'^profile/add_profession/$', views.add_profession, name='add_profession'),
                       url(r'^profile/add_profession/(?P<selected_character>.+)/$', views.add_profession, name='add_profession'),
                       url(r'^profile/delete_profession/$', views.delete_profession, name='delete_profession'),
                       url(r'^profile/delete_profession/(?P<selected_character>.+)/$', views.delete_profession, name='delete_profession'),
                       url(r'^profile/delete_profession/(?P<selected_character>.+)/(?P<selected_profession>.+)/$', views.delete_profession, name='delete_profession'),
                       )
