from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib.auth.models import User
from guilds.views import join_guild


def inbox(request):
    userprofile = User.objects.get(username=request.user.username).userprofile
    notification_list = userprofile.notification_set.all()
    guildinvite_list = userprofile.guildinvite_set.all()

    context = RequestContext(request, {'user': request.user, 'request': request,
                                       'notification_list': notification_list, 'guildinvite_list': guildinvite_list})

    return render_to_response('notifications/inbox.html', context_instance=context)


def delete_notification(request, selected_notification=None):
    userprofile = User.objects.get(username=request.user.username).userprofile
    target_notification = userprofile.notification_set.get(id=selected_notification)
    target_notification.delete()

    return redirect(reverse('notifications:inbox'))


def guildinvite_response(request, response=None, guildinvite_id=None):
    userprofile = User.objects.get(username=request.user.username).userprofile
    target_invite = userprofile.guildinvite_set.get(id=guildinvite_id)
    target_invite.delete()

    if response == 'accept':
        join_guild(userprofile, target_invite.guild)

    return redirect(reverse('notifications:inbox'))
