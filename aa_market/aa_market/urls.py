from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aa_market.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lfw/', include('workorder.urls', namespace='workorder')),
    url(r'^profile/', include('userprofile.urls', namespace='userprofile')),
    url(r'^guilds/', include('guilds.urls', namespace='guilds')),
    url(r'^notifications/', include('notifications.urls', namespace='notifications')),
    url(r'^$', include('workorder.urls', namespace='workorder')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)
