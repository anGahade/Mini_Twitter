from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from custom_user.models import CustomUser
from users.models import User


class UserListView(ListView):
    model = CustomUser
    template_name = 'users/users_list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        if self.kwargs.get('username'):
            return CustomUser.objects.filter(username=self.kwargs['username'])
        else:
            return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('username'):
            context['title'] = f'Information about {self.kwargs["username"]}:'
        else:
            context['title'] = 'List of users:'
        return context




