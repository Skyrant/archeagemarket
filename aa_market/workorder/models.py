from django.db import models
from django import forms
from userprofile.models import Character


class Profession(models.Model):
    character = models.ForeignKey(Character)
    profession = models.CharField(max_length=100)
    skill = models.IntegerField(max_length=6)

    def __str__(self):
        return self.profession + " : " + str(self.skill)


class AddProfessionForm(forms.Form):

    def __init__(self, choices, *args, **kwargs):
        super(AddProfessionForm, self).__init__(*args, **kwargs)
        self.fields["character"] = forms.ChoiceField(choices=choices)

    profession = forms.ChoiceField()
    profession.choices = (
        ('cooking', 'Cooking'),
        ('fishing', 'Fishing'),
        ('alchemy', 'Alchemy'),
        ('weaponry', 'Weaponry'),
        ('carpentry', 'Carpentry'),
        ('metalwork', 'Metalwork'),
        ('leatherwork', 'Leatherwork'),
        ('tailoring', 'Tailoring'),
        ('handicrafts', 'Handicrafts'),
        ('construction', 'Construction'),
        ('machining', 'Machining'),
        ('commerce', 'Commerce'),
        ('farming', 'Farming'),
        ('husbandry', 'Husbandry'),
        ('masonry', 'Masonry'),
        ('gathering', 'Gathering'),
        ('logging', 'Logging'),
        ('mining', 'Mining'),
        ('printing', 'Printing'),
        ('larceny', 'Larceny'),
        ('composition', 'Composition'),
    )
    skill = forms.IntegerField(max_value=100000)


class DeleteProfessionForm(forms.Form):

    def __init__(self, character_choices, *args, **kwargs):
        profession_choices = (
            ('cooking', 'Cooking'),
            ('fishing', 'Fishing'),
            ('alchemy', 'Alchemy'),
            ('weaponry', 'Weaponry'),
            ('carpentry', 'Carpentry'),
            ('metalwork', 'Metalwork'),
            ('leatherwork', 'Leatherwork'),
            ('tailoring', 'Tailoring'),
            ('handicrafts', 'Handicrafts'),
            ('construction', 'Construction'),
            ('machining', 'Machining'),
            ('commerce', 'Commerce'),
            ('farming', 'Farming'),
            ('husbandry', 'Husbandry'),
            ('masonry', 'Masonry'),
            ('gathering', 'Gathering'),
            ('logging', 'Logging'),
            ('mining', 'Mining'),
            ('printing', 'Printing'),
            ('larceny', 'Larceny'),
            ('composition', 'Composition'),
        )
        super(DeleteProfessionForm, self).__init__(*args, **kwargs)
        self.fields["character"] = forms.ChoiceField(choices=character_choices)
        self.fields["profession"] = forms.ChoiceField(choices=profession_choices)

    profession = forms.ChoiceField()


class FindProfessionForm(forms.Form):

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
    profession = forms.ChoiceField()
    profession.choices = (
        ('cooking', 'Cooking'),
        ('fishing', 'Fishing'),
        ('alchemy', 'Alchemy'),
        ('weaponry', 'Weaponry'),
        ('carpentry', 'Carpentry'),
        ('metalwork', 'Metalwork'),
        ('leatherwork', 'Leatherwork'),
        ('tailoring', 'Tailoring'),
        ('handicrafts', 'Handicrafts'),
        ('construction', 'Construction'),
        ('machining', 'Machining'),
        ('commerce', 'Commerce'),
        ('farming', 'Farming'),
        ('husbandry', 'Husbandry'),
        ('masonry', 'Masonry'),
        ('gathering', 'Gathering'),
        ('logging', 'Logging'),
        ('mining', 'Mining'),
        ('printing', 'Printing'),
        ('larceny', 'Larceny'),
        ('composition', 'Composition'),
    )
    minimum_skill = forms.IntegerField(max_value=100000)
