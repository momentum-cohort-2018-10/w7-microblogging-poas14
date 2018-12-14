from django.contrib import admin
from core.models import User, Post, Like, Follow

# Register your models here.

class FollowersInline(admin.StackedInline):
    verbose_name = "Followers"
    model = Follow
    fk_name = "followed_by"
    fields = ("following",)
    extra = 1

class FollowingInline(admin.StackedInline):
    verbose_name = "Following"
    model = Follow
    fk_name = "following"
    fields = ("followed_by",)
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'created_at']

class UserAdmin(admin.ModelAdmin):
    fields = ("username", "email", "is_superuser", "is_staff")
    inlines = [FollowersInline, FollowingInline]


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)