from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from comments.forms import CommentForm
from comments.models import Comment
from posts.models import Post


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comments_list.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        if self.kwargs.get('username'):
            return Comment.objects.filter(user__username=self.kwargs['username'])
        elif self.kwargs.get('post_id'):
            return Comment.objects.filter(post__id=self.kwargs['post_id'])
        else:
            return Comment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('username'):
            context['title'] = f'List of comments by {self.kwargs["username"]}:'
        elif self.kwargs.get('post_id'):
            post = Comment.objects.filter(post__id=self.kwargs['post_id']).first()
            context['title'] = f'Comment on post: {post.post.title}' if post else 'List of comments:'
        else:
            context['title'] = 'List of comments:'
        return context


# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'comments/add_comment.html'
#     success_url = reverse_lazy('comments:comments_list')
#
#     def get_form_kwargs(self):
#         form_kwargs = super().get_form_kwargs()
#         form_kwargs['post_id'] = self.kwargs.get('post_id')
#         return form_kwargs
#
#     def form_valid(self, form):
#         post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
#         form.instance.user = self.request.user
#         form.instance.post = post
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post_id'] = self.kwargs.get('post_id')
#         return context
#
#     def get(self, request, *args, **kwargs):
#         post_id = self.kwargs.get('post_id')
#         if post_id is None:
#             return redirect('comments:comments_list')
#         return super().get(request, *args, **kwargs)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/add_comment.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.user = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse_lazy('posts:post_detail', kwargs={'pk': post_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.kwargs.get('post_id')
        return context


