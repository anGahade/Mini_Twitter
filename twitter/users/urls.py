from django.urls import path

from .views import users_list

app_name = "users"
urlpatterns = [
    path('users_list', users_list, name="users_list"),
    path('/<str:username>/', users_list, name="users_list"),
    ]
