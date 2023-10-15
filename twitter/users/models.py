from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="users/profile_images", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User: {self.username}'