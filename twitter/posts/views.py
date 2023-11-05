from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from posts.forms import PostForm
from posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        if self.kwargs.get('username'):
            return Post.objects.filter(user__username=self.kwargs['username'])
        elif self.kwargs.get('post_id'):
            return Post.objects.filter(id=self.kwargs['post_id'])
        else:
            return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('username'):
            context['title'] = f'List of posts by {self.kwargs["username"]}:'
        elif self.kwargs.get('post_id'):
            context['title'] = f'Post # {self.kwargs["post_id"]}:'
        else:
            context['title'] = 'List of posts:'
        return context


# def add_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:post_list')
#     else:
#         form = PostForm()
#     return render(request, 'posts/add_post.html', {'form': form})


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the current user to the post
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

class HomeView(TemplateView):
    template_name = 'posts/home.html'







