from ..models import UserProfile


def user_details(details, response, user=None, *args, **kwargs):
    if user:
        if kwargs['is_new']:
            attrs = {'user': user}
            UserProfile.objects.create(**attrs)