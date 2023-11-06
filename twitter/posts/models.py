from django.db import models
from custom_user.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, through='Like', related_name='liked_posts')

    def add_like(self, user):
        like, created = Like.objects.get_or_create(user=user, post=self)
        return like

    def remove_like(self, user):
        Like.objects.filter(user=user, post=self).delete()


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
