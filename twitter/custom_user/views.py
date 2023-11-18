from account.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from account.views import SettingsView
from django.contrib import messages

from .models import CustomUser


def subscribe(request, username):
    user_to_subscribe = get_object_or_404(CustomUser, username=username)
    request.user.follow(user_to_subscribe)
    return redirect('custom_user:user_profile', username=username)


def unsubscribe(request, username):
    user_to_unsubscribe = get_object_or_404(CustomUser, username=username)
    request.user.unfollow(user_to_unsubscribe)
    return redirect('custom_user:user_profile', username=username)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'bio')


class CustomSettingsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    template_name = 'custom_user/custom_settings.html'
    form_class = CustomUserChangeForm
    context_object_name = 'user'
    success_message = 'Profile updated successfully.'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('custom_user:user_profile', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        print(f"User {self.object.username} registered and logged in.")
        return response

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     messages.success(self.request, 'Profile updated successfully.')
    #     return response


class CustomUserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'custom_user/user_profile.html'
    context_object_name = 'custom_user'

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile_user = self.get_object()

        # Перевірка чи користувач вже підписаний на профіль
        context['is_following'] = user.is_authenticated and user in profile_user.followers.all()

        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile_user = self.get_object()

        # Логіка додавання та видалення підписки
        if 'subscribe' in request.POST:
            profile_user.followers.add(user)
        elif 'unsubscribe' in request.POST:
            profile_user.followers.remove(user)

        return redirect('custom_user:user_profile', username=profile_user.username)


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('posts:home')
    template_name = 'custom_user/registration.html'

    def form_valid(self, form):
        # Перевірка наявності користувача з вказаною електронною адресою
        email = form.cleaned_data.get('email')
        existing_user = CustomUser.objects.filter(email=email).first()

        if existing_user:
            form.add_error('email', 'Користувач з такою електронною адресою вже існує.')
            return self.form_invalid(form)

        response = super().form_valid(form)
        login(self.request, self.object)
        return response


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('posts:home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'custom_user/login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

