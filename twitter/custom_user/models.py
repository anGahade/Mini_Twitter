from django.db import models
from django.contrib.auth.models import AbstractUser


class Follower(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='following_set')
    follower = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='followers_set')
    created_at = models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.CharField(max_length=125, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, through=Follower, related_name='following')
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_user_set', related_query_name='custom_user', verbose_name='groups')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_user_set', related_query_name='custom_user', verbose_name='user permissions')

    def follow(self, user):
        follower, created = Follower.objects.get_or_create(user=user, follower=self)
        return created

    def unfollow(self, user):
        Follower.objects.filter(user=user, follower=self).delete()

    def is_following(self, user):
        return Follower.objects.filter(user=user, follower=self).exists()

    def followers_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()