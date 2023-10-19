from django.urls import path

from .views import comments_list, add_comment

app_name = "comments"
urlpatterns = [
    path('', comments_list, name="index"),
    path('/<str:username>/', comments_list, name="user_comments_list"),
    path('add-comment/', add_comment, name="add_comment"),
]
