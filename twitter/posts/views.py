from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from posts.forms import PostForm
from posts.models import Post


def post_list(request, username=None):
    if username:
        posts = Post.objects.filter(user__username=username)
        title = f'List of posts by {username}:'
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
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})




