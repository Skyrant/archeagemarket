from django.db import models
from django import forms
from userprofile.models import UserProfile


class GuildInviteForm(forms.Form):
    target = forms.CharField(max_length=64)


class AddGuildForm(forms.Form):
    guild_name = forms.CharField(max_length=32)
    server = forms.ChoiceField()
    server.choices = (
        ('aranzeb', 'Aranzeb'),
        ('calleil', 'Calleil'),
        ('enla', 'Enla'),
        ('ezi', 'Ezi'),
        ('inoch', 'Inoch'),
        ('kyrios', 'Kyrios'),
        ('lucius', 'Lucius'),
        ('naima', 'Naima'),
        ('ollo', 'Ollo'),
        ('salphira', 'Salphira'),
        ('tahyang', 'Tahyang')
    )


class DeleteGuildForm(forms.Form):
    confirm = forms.BooleanField(required=True, help_text="Are you sure you want to delete the guild?")


class LeaveGuildForm(forms.Form):
    confirm = forms.BooleanField(required=True, help_text="Are you sure you want to leave the guild?")


class Guild(models.Model):
    user_profile = models.OneToOneField(UserProfile, unique=True, related_name='guild_leader', null=True, on_delete=models.SET_NULL)
    guild_name = models.CharField(max_length=32)
    server = models.CharField(max_length=100)
