from django.urls import path

from .views import UserListView

app_name = "users"
urlpatterns = [
    path('users_list', UserListView.as_view(), name="users_list"),
    path('/<str:username>/', UserListView.as_view(), name="users_list"),
    ]
