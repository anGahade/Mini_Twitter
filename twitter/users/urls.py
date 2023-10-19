from django.urls import path

from .views import users_list

app_name = "users"
urlpatterns = [
    path('', users_list, name="index"),
    path('/<str:username>/', users_list, name="users_list"),
    ]
