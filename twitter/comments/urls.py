from django.urls import path

from .views import CommentListView, CommentCreateView

app_name = "comments"
urlpatterns = [
    path('', CommentListView.as_view(), name="comments_list"),
    path('user/<str:username>/', CommentListView.as_view(), name="user_comments_list"),
    path('post/<int:post_id>/', CommentListView.as_view(), name="post_comments_list"),
    path('add-comment/<int:post_id>/', CommentCreateView.as_view(), name="add_comment"),
    path('post/<int:pk>/', CommentListView.as_view(), name='comment_list'),
]
