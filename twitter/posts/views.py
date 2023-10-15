from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


# def index(request):
#     posts = Post.objects.all()
#     context = {'posts': posts, 'title': 'List of posts:'}
#     return render(request, 'posts_t/posts_list.html', context)
def index(request, username=None):
    if username:
        posts = Post.objects.filter(user__username=username)
        title = f'List of posts by {username}:'
    else:
        posts = Post.objects.all()
        title = 'List of posts:'

    context = {'posts': posts, 'title': title}
    return render(request, 'posts_t/posts_list.html', context)


def test(request):
    return HttpResponse("<h1>Test title</h1>")

