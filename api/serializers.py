from rest_framework import serializers
from core.models import User, Post, Follow, Like

class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            value, _ = self.get_queryset().get_or_create(**{self.slug_field: data})
            return value
        except (TypeError, ValueError):
            self.fail("invalid")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'text', 'created_at', 'id')

class FollowSerializer(serializers.ModelSerializer):
    followed_user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ("followed_user",)