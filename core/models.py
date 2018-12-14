from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    users_followed = models.ManyToManyField(
        to="User",
        through="Follow",
        through_fields=("followed_by", "following"),
        related_name="followers",
    )

class Follow(models.Model):
    followed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows_from')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows_to')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')