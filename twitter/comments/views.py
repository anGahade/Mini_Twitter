from django.http import HttpResponse
from django.shortcuts import render
from comments.models import Comment


def index(request):
    comments = Comment.objects.all()
    context = {'comments': comments, 'title': 'List of comments:'}
    return render(request, 'comments/comments_list.html', context)


def test(request):
    return HttpResponse("<h1>Test title</h1>")

