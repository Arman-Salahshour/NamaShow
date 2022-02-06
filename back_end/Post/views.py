from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from Core.models import Post
from Post import serializers

# Create your views here.


class PostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = serializers.PostSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()


class PostRetrieveViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PostRetrieveSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    lookup_field = 'postID'

    def get_queryset(self):
        return self.queryset