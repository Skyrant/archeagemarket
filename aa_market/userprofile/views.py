from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.shortcuts import render, render_to_response, redirect
from userprofile.models import AddCharacterForm, Character, DeleteCharacterForm
# Create your views here.


def add_character(request):
    #TODO: Add unique check for dupe names.
    if request.method == "POST":
        form = AddCharacterForm(request.POST)

        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            c = Character(character_name=form.cleaned_data['character_name'], server=form.cleaned_data['server'], user_profile_id=user.userprofile.id)
            c.save()
            return redirect(reverse('userprofile:profile'))

    else:
        form = AddCharacterForm()

    return render(request, 'userprofile/add_character.html', {'form': form})


def delete_character(request, selected_character=None):
    error = None

    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        characters = user.userprofile.character_list(user)
        form = DeleteCharacterForm(characters, request.POST)

        if form.is_valid():
            character_name = form.cleaned_data['character']
            character = user.userprofile.character_set.get(character_name=character_name)
            character.delete()

            return redirect(reverse('userprofile:profile'))

    else:
        user = User.objects.get(username=request.user.username)
        characters = user.userprofile.character_list(user)
        if not characters:
            error = "You have no characters to delete!"

        if selected_character is not None:
            form = DeleteCharacterForm(characters, initial={'character': selected_character})

        else:
            form = DeleteCharacterForm(characters)

    return render(request, 'userprofile/delete_character.html', {'form': form, 'error': error})


def profile(request):
    character_list = request.user.userprofile.get_characters()

    context = RequestContext(request, {'user': request.user, 'request': request, 'character_list': character_list})
    return render_to_response('userprofile/profile.html', context_instance=context)
