from django.conf.urls import patterns, url
from guilds import views

urlpatterns = patterns('',
                       url(r'^add_guild/$', views.add_guild, name='add_guild'),
                       url(r'^delete_guild/$', views.delete_guild, name='delete_guild'),
                       url(r'^guild_invite/$', views.invite_to_guild, name='guild_invite'),
                       url(r'^leave_guild/$', views.leave_guild, name='leave_guild'),
                       url(r'^guild_profile/$', views.guild_profile, name='guild_profile'),
                       url(r'^guild_kick/$', views.remove_from_guild, name='remove_from_guild'),
                       url(r'^guild_kick/(?P<target>.+)/$', views.remove_from_guild, name='remove_from_guild'),
                       url(r'^promote/$', views.promote_to_officer, name='promote'),
                       url(r'^promote/(?P<target>.+)/$', views.promote_to_officer, name='promote'),
                       )
