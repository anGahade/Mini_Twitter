from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model


from posts.forms import PostForm
from posts.models import Post


def post_list(request, username=None, post_id=None):
    if username:
        posts = Post.objects.filter(user__username=username)
        title = f'List of posts by {username}:'
    elif post_id:
        posts = Post.objects.filter(id=post_id)
        title = f'Post # {post_id}:'
    else:
        posts = Post.objects.all()
        title = 'List of posts:'

    context = {'posts': posts, 'title': title}
    return render(request, 'posts/posts_list.html', context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})


def home(request):
    return render(request, 'posts/home.html')







