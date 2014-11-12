from django.db import models
from userprofile.models import UserProfile
from guilds.models import Guild


class Notification(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    subject = models.TextField(max_length=64)
    text = models.TextField(max_length=256)
    seen = models.BooleanField(default=False)


class GuildInvite(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    guild = models.OneToOneField(Guild)
