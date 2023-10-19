from django.http import HttpResponse
from django.shortcuts import render
from users.models import User


def users_list(request, username=None):
    if username:
        users = User.objects.filter(username=username)
        title = f'Information about {username}:'
    else:
        users = User.objects.all()
        title = 'List of users:'
    context = {'users': users, 'title': title}
    return render(request, 'users/users_list.html', context)




