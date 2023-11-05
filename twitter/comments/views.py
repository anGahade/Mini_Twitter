from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from comments.forms import CommentForm
from comments.models import Comment


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


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/add_comment.html'
    success_url = reverse_lazy('comments:comments_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)