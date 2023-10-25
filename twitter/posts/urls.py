from django.urls import path

from .views import post_list, add_post, home

app_name = "posts"
urlpatterns = [
    path('', home, name="home"),
    path('/<str:username>/', post_list, name="user_posts_list"),
    path('<int:post_id>/', post_list, name="post_id_list"),
    path('add-post/', add_post, name="add_post"),
    path('home/', home, name="home"),
    path('post_list', post_list, name="post_list"),
    path('user/<int:user_id>/posts/', user_posts, name='user_posts')
]
