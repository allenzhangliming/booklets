from .models import Tag, Bookmark
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TagSerializer, BookmarkSerializer, UserSerializer
from .permissions import IsOwnerOrReadonly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_list', request=request, format=format),
        'tags': reverse('tag_list', request=request, format=format),
        'bookmarks': reverse('bookmark_list', request=request, format=format)
    })

class TagList(generics.ListCreateAPIView):
    """
    List all tags, or create a new tag
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a Tag
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class BookmarkList(generics.ListCreateAPIView):
    """
    List all tags, or create a new tag
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly)
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookmarkDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a Tag
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly)
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a user
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly)
    queryset = User.objects.all()
    serializer_class = UserSerializer