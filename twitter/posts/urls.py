from django.urls import path

from .views import post_list, add_post

app_name = "posts"
urlpatterns = [
    path('', post_list, name="post_list"),
    path('post/<str:username>/', post_list, name="user_posts_list"),
    path('add-post/', add_post, name="add_post"),
]
