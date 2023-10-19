from django.http import HttpResponse
from django.shortcuts import render, redirect

from comments.forms import CommentForm
from comments.models import Comment


def comments_list(request, username=None, post_id=None):
    if username:
        comments = Comment.objects.filter(user__username=username)
        title = f'List of comments by {username}:'
    elif post_id:
        comments = Comment.objects.filter(post__id=post_id)
        title = f'List of comments to a post {post_id}:'
    else:
        comments = Comment.objects.all()
        title = 'List of comments:'

    context = {'comments': comments, 'title': title}
    return render(request, 'comments/comments_list.html', context)


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('comments:comments_list')
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form})
