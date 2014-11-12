from django.conf.urls import patterns, url, include
from userprofile import views

urlpatterns = patterns('',
                       url(r'^$', views.profile, name='profile'),
                       url(r'^add_character/$', views.add_character, name='add_character'),
                       url(r'^delete_character/$', views.delete_character, name='delete_character'),
                       url(r'^delete_character/(?P<selected_character>.+)/$', views.delete_character, name='delete_character'),
                       )
