from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from guilds.models import Guild, AddGuildForm, DeleteGuildForm, GuildInviteForm, LeaveGuildForm
from notifications.models import GuildInvite
import traceback

#TODO: Demote user | What happens if I kick a guild leader?


def add_guild(request):
    error = None
    user = User.objects.get(username=request.user.username)

    if request.method == "POST":
        form = AddGuildForm(request.POST)

        if form.is_valid():
            g = Guild(guild_name=form.cleaned_data['guild_name'], server=form.cleaned_data['server'], user_profile_id=user.userprofile.id)
            g.save()
            user.userprofile.guild_id = g.id
            user.userprofile.member_of = g
            g.officers.add(user.userprofile)
            user.userprofile.save()
            return redirect(reverse('userprofile:profile'))

    else:
        if user.userprofile.member_of:
            error = "You already have a guild."
            form = None

        else:
            form = AddGuildForm()

    return render(request, 'guilds/add_guild.html', {'form': form, 'error': error})


def join_guild(up, g):
    up.member_of = g
    up.save()


def delete_guild(request):
    error = None
    user = User.objects.get(username=request.user.username)

    if request.method == "POST":
        userprofile = user.userprofile
        form = DeleteGuildForm(request.POST)

        if form.is_valid() and userprofile.guild_leader:
            g = user.userprofile.guild_leader
            g.delete()
            return redirect(reverse('userprofile:profile'))

    else:
        if not user.userprofile.member_of:
            error = "You have no guild to delete."
            form = None
        else:
            form = DeleteGuildForm()

    return render(request, 'guilds/delete_guild.html', {'form': form, 'error': error})


def leave_guild(request):
    error = None
    user = User.objects.get(username=request.user.username)

    if request.method == "POST":
        form = LeaveGuildForm(request.POST)

        if form.is_valid():
            g = user.userprofile.member_of
            g.members.remove(user.userprofile)
            return redirect(reverse('userprofile:profile'))

    else:
        if not user.userprofile.member_of:
            error = "You have no guild to leave."
            form = None
        else:
            form = LeaveGuildForm()

    return render(request, 'guilds/leave_guild.html', {'form': form, 'error': error})


def invite_to_guild(request):
    error = None

    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        form = GuildInviteForm(request.POST)

        if form.is_valid():
            target = form.cleaned_data['target']
            try:
                target_user = User.objects.get(username=target)
                target_profile = target_user.userprofile
                target_guild = user.userprofile.member_of

                if user.userprofile.officers:
                    guild_invite = GuildInvite(user_profile=target_profile, guild=target_guild)
                    guild_invite.save()
                else:
                    error = "You do not have invite privileges."
                    return render(request, 'guilds/guild_invite.html', {'form': form, 'error': error})

            except:
                print(traceback.format_exc())
                error = "This target does not exist."
                return render(request, 'guilds/guild_invite.html', {'form': form, 'error': error})

            return redirect(reverse('userprofile:profile'))

    else:
        form = GuildInviteForm()

    return render(request, 'guilds/guild_invite.html', {'form': form, 'error': error})


def remove_from_guild(request, target=None):
    error = None
    user = User.objects.get(username=request.user.username)

    if user.userprofile.officers:
        target_user = User.objects.get(username=target)
        target_profile = target_user.userprofile

        g = user.userprofile.member_of

        if g == target_profile.member_of:
            g.members.remove(target_profile)

    return render(request, 'guilds/remove_from_guild.html', {'error': error, 'target': target})


def promote_to_officer(request, target=None):
    error = None
    user = User.objects.get(username=request.user.username)

    if user.userprofile.officers:
        target_user = User.objects.get(username=target)
        target_profile = target_user.userprofile

        g = user.userprofile.member_of

        if g == target_profile.member_of:
            g.officers.add(target_profile)

    return render(request, 'guilds/promote.html', {'error': error, 'target': target})


def guild_profile(request):
    error = None
    user = User.objects.get(username=request.user.username)
    g = user.userprofile.member_of
    members = g.members.all()
    is_officer = False

    if user.userprofile.officers:
        is_officer = True

    return render(request, 'guilds/guild_profile.html', {'error': error, 'members': members, 'is_officer': is_officer})
