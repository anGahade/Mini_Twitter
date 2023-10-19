from django.urls import path

from .views import comments_list, add_comment

app_name = "comments"
urlpatterns = [
    path('', comments_list, name="comments_list"),
    path('/<str:username>/', comments_list, name="user_comments_list"),
    path('<int:post_id>/', comments_list, name="post_comments_list"),
    path('add-comment/', add_comment, name="add_comment"),
]
