from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.utils import serializer_helpers
from Core.models import Celebrity, Genre, Film
from Film import serializers

# Create your views here.


class GenreViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    """ In case we want to make access to this list available to users only. """
#   permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer

    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()


class CelebrityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    """ In case we want to make access to this list available to users only. """
#   permission_classes = (IsAuthenticated,)
    queryset = Celebrity.objects.all()
    serializer_class = serializers.CelebritySerializer

    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()


class FilmViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    """ In case we want to make access to this list available to users only. """
#   permission_classes = (IsAuthenticated,)
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer

    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()