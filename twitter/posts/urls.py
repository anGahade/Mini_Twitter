from django.urls import path

from .views import index, test

app_name = "posts"
urlpatterns = [
    path('', index, name="index"),
    path('test/', test, name="test"),
    path('<str:username>/', index, name="user_posts_list"),
]
