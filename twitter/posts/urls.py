from django.urls import path

from .views import index, post_detail, add_post

app_name = "posts"
urlpatterns = [
    path('', index, name="index"),
    path('<str:username>/', index, name="user_posts_list"),
    path('posts/<int:user_id>', post_detail, name="post_detail"),
    path('posts/add_post', add_post, name="add_post"),
]
