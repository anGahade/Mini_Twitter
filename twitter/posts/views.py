from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from posts.forms import PostForm
from posts.models import Post
from comments.models import Comment


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

        posts = context['posts']
        comments_count = [post.comments.count() for post in posts]
        context['comments_count'] = comments_count

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    success_url = 'http://127.0.0.1:8000/post_list'  # Замініть '/success-url/' на реальний URL

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('custom_user:login')  # редирект на сторінку логіну

        return super().dispatch(request, *args, **kwargs)


class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def test_func(self):
        return True


class HomeView(TemplateView):
    template_name = 'posts/home.html'


class LikePostView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('posts:post_list')


class EditPostView(LoginRequiredMixin, View):
    template_name = 'posts/edit_post.html'
    success_url = reverse_lazy('posts:post_list')

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, user=request.user)
        form = PostForm(instance=post)
        return render(request, self.template_name, {'form': form, 'post_id': post_id})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, user=request.user)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', pk=post_id)
        return render(request, self.template_name, {'form': form, 'post_id': post_id})


class DeletePostView(LoginRequiredMixin, View):
    template_name = 'posts/delete_post.html'

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, user=request.user)
        return render(request, self.template_name, {'post': post})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, user=request.user)
        post.delete()
        return redirect('posts:post_list')


@login_required
def get_posts_by_following(request):
    following = request.user.following.all()
    posts = Post.objects.filter(user__in=following)
    return posts


class PostsByFollowingView(View):
    template_name = 'posts/posts_by_following.html'

    def get(self, request, *args, **kwargs):
        posts = get_posts_by_following(request)
        return render(request, self.template_name, {'posts': posts})
