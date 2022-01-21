from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.utils import serializer_helpers
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from Core.models import Celebrity, Genre, Film, Video
from Film import serializers
from Core.OMDBcrawler import search_omdb


# Create your views here.


class GenreViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = serializers.GenreSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Genre.objects.all()
    pagination_class = PageNumberPagination


    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()


class GenreRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GenreRetrieveSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Genre.objects.all()
    lookup_field = 'genreID'

    def get_queryset(self):
        return self.queryset


class CelebrityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Celebrity.objects.all()
    serializer_class = serializers.CelebritySerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()


class CelebrityRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = serializers.CelebrityRetrieveSerializer
    queryset = Celebrity.objects.all()
    lookup_field = 'celebID'

    def get_queryset(self):
        return self.queryset


class FilmViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Film.objects.all()
    serializer_class = serializers.FilmListSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return self.queryset.order_by('-releaseDate')
    
    def perform_create(self, serializer):
        serializer.save()


class FilmCreateViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Film.objects.none()
    serializer_class = serializers.FilmCreateSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return self.queryset.order_by('-releaseDate')
    
    def perform_create(self, serializer):
        serializer.save()


class FilmRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = serializers.FilmRetrieveSerializer
    queryset = Film.objects.all()
    lookup_field = 'filmID'

    def get_queryset(self):
        return self.queryset


class VideoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer

    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()


class VideoRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = serializers.VideoSerializer
    queryset = Video.objects.all()
    lookup_field = 'videoID'

    def get_queryset(self):
        return self.queryset