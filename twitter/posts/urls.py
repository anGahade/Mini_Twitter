from django.urls import path

from .views import PostListView, PostCreateView, HomeView, PostDetailView

app_name = "posts"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('user/<str:username>/', PostListView.as_view(), name="user_posts_list"),
    path('<int:post_id>/', PostListView.as_view(), name="post_id_list"),
    path('add-post/', PostCreateView.as_view(), name="add_post"),
    path('home/', HomeView.as_view(), name="home"),
    path('post_list', PostListView.as_view(), name="post_list"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
