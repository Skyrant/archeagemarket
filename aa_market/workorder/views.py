from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template.context import RequestContext
from workorder.models import AddProfessionForm, Profession, DeleteProfessionForm, FindProfessionForm


def find_profession(request):
    if request.method == "POST":
        form = FindProfessionForm(request.POST)

        if form.is_valid():
            profession = form.cleaned_data['profession']
            minimum_skill = form.cleaned_data['minimum_skill']
            server = form.cleaned_data['server']
            results = Profession.objects.filter(character__server=server).filter(profession=profession).filter(skill__gte=minimum_skill).order_by('-skill')

            return render(request, 'workorder/found_profession.html', {'profession': profession, 'results': results})

    else:
        form = FindProfessionForm()

    return render(request, 'workorder/find_profession.html', {'form': form})


def add_profession(request, selected_character=None):
    error = None

    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        characters = user.userprofile.character_list(user)
        form = AddProfessionForm(characters, request.POST)

        if form.is_valid():
            character_name = form.cleaned_data['character']
            profession = form.cleaned_data['profession']
            skill = form.cleaned_data['skill']
            character = user.userprofile.character_set.get(character_name=character_name)

            if character.has_profession(profession):
                prof = character.profession_set.get(profession=profession)
                prof.skill = skill
                prof.save()

            else:
                p = Profession(profession=profession, character_id=character.id, skill=skill)
                p.save()

            return redirect(reverse('userprofile:profile'))

    else:
        user = User.objects.get(username=request.user.username)
        characters = user.userprofile.character_list(user)
        if not characters:
            error = "You have no characters, make a character first!"
        if selected_character is not None:
            form = AddProfessionForm(characters, initial={'character': selected_character})
        else:
            form = AddProfessionForm(characters)

    return render(request, 'workorder/add_profession.html', {'form': form, 'error': error})


def delete_profession(request, selected_character=None, selected_profession=None):
    error = None

    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        characters = user.userprofile.character_list(user)
        form = DeleteProfessionForm(characters, request.POST)

        if form.is_valid():
            character_name = form.cleaned_data['character']
            profession = form.cleaned_data['profession']
            character = user.userprofile.character_set.get(character_name=character_name)

            if character.has_profession(profession):
                prof = character.profession_set.get(profession=profession)
                prof.delete()

            return redirect(reverse('userprofile:profile'))

    else:
        user = User.objects.get(username=request.user.username)
        characters = user.userprofile.character_list(user)
        if not characters:
            error = "You have no characters, so there's nothing to delete!"
        if selected_character is not None and selected_profession is not None:
            form = DeleteProfessionForm(characters, initial={'character': selected_character, 'profession':selected_profession})
        elif selected_character is not None and selected_profession is None:
            form = DeleteProfessionForm(characters, initial={'character': selected_character})
        else:
            form = DeleteProfessionForm(characters)

    return render(request, 'workorder/delete_profession.html', {'form': form, 'error': error})


def index(request):
    context = RequestContext(request, {'user': request.user, 'request': request})
    return render_to_response('workorder/index.html', context_instance=context)


