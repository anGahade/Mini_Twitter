from django.db import models
from custom_user.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)



