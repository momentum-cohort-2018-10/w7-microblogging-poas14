from django.urls import path
from api import views as api_views


urlpatterns = [
    # path("", api_views.)
    path("posts/", api_views.PostListCreateView.as_view(), name="api_post_list"),
    path("users/", api_views.UserListView.as_view(), name="api_user_list"),
    path("follows/", api_views.FollowListCreateView.as_view(), name="api_follow_list"),
    # path(
    #     "follows/<str:username>/",
    #     api_views.FollowDestroyView.as_view(),
    #     name="api_follow",
    # ),
]