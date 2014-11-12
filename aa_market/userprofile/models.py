from django.db import models
from django import forms
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    reputation = models.IntegerField(max_length=32, default=0)
    member_of = models.ForeignKey('guilds.Guild', null=True, related_name='members', on_delete=models.SET_NULL)
    officers = models.ForeignKey('guilds.Guild', null=True, related_name='officers', on_delete=models.SET_NULL)

    def character_list(self, user):
        characters = user.userprofile.character_set.all()
        character_list = []

        for c in characters:
            character_list.append((str(c.character_name), str(c.character_name)))

        return character_list

    def get_characters(self):
        return self.user.userprofile.character_set.all()


class Character(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    character_name = models.CharField(max_length=100, unique=True)
    server = models.CharField(max_length=100)

    def __str__(self):
        return self.character_name + ':' + self.server

    def get_professions(self):
        return self.profession_set.all()

    def has_profession(self, profession):
        for p in self.profession_set.all():
            if p.profession == profession:
                return True

        return False

    professions = property(get_professions)


class AddCharacterForm(forms.Form):
    character_name = forms.CharField(max_length=100)
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


class DeleteCharacterForm(forms.Form):

    def __init__(self, choices, *args, **kwargs):
        super(DeleteCharacterForm, self).__init__(*args, **kwargs)
        self.fields["character"] = forms.ChoiceField(choices=choices)
