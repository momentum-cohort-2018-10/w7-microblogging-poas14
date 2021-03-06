from core.models import Post, Follow, User
from api.serializers import PostSerializer, UserSerializer, FollowSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import generics

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.request.user.posts

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AllUserListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class FollowListCreateView(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        return self.request.user.follows_from

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    """
    Retrieve, update or delete a code post.
    """
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(serializer.data)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('posts', request=request, format=format),
#         'posts': reverse('users', request=request, format=format)
#     })