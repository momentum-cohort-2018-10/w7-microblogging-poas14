from django.urls import path
from api import views as api_views


urlpatterns = [
    # path("", api_views.)
    # path("posts/<str:username>/", api_views.PostListCreateView.as_view(), name="api_post_list"),
    path('posts/<int:id>', api_views.post_detail),
    path("posts/", api_views.AllUserListView.as_view(), name="all_posts"),
    path("users/", api_views.UserListView.as_view(), name="api_user_list"),
    path("follows/", api_views.FollowListCreateView.as_view(), name="api_follow_list"),
    # path(
    #     "follows/<str:username>/",
    #     api_views.FollowDestroyView.as_view(),
    #     name="api_follow",
    # ),
]