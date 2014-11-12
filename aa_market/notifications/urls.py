from django.conf.urls import patterns, url, include
from notifications import views

urlpatterns = patterns('',
                       url(r'^$', views.inbox, name='inbox'),
                       url(r'^delete_notification/$', views.delete_notification, name='delete_notification'),
                       url(r'^delete_notification/(?P<selected_notification>.+)/$', views.delete_notification, name='delete_notification'),
                       url(r'^response/$', views.guildinvite_response, name='guildinvite_response'),
                       url(r'^response/(?P<response>.+)/(?P<guildinvite_id>.+)/$', views.guildinvite_response, name='guildinvite_response'),
                       )
