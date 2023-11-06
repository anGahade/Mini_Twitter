from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
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



class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class HomeView(TemplateView):
    template_name = 'posts/home.html'


class LikePostView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.likes.filter(id=request.user.id).exists():
            # Користувач вже лайкнув цей пост, тому видалити лайк
            post.likes.remove(request.user)
        else:
            # Користувач ще не лайкав цей пост, тому додати лайк
            post.likes.add(request.user)
        return redirect('posts:post_list')






