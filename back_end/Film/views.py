from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from Core.models import Celebrity, FilmPurchase, Genre, Film, Video
from Film import serializers

# Create your views here.


# Genre
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


# Genre Retrieve
class GenreRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GenreRetrieveSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Genre.objects.all()
    lookup_field = 'genreID'

    def get_queryset(self):
        return self.queryset

# Celebrity
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

# Celebrity Retrieve
class CelebrityRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = serializers.CelebrityRetrieveSerializer
    queryset = Celebrity.objects.all()
    lookup_field = 'celebID'

    def get_queryset(self):
        return self.queryset


# Film List
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


# Film Create
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


# Film Retrieve
class FilmRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.FilmRetrieveSerializer
    queryset = Film.objects.all()
    lookup_field = 'filmID'

    def get_queryset(self):
        return self.queryset


# Video
class VideoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer

    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()


# Video Retrieve
class VideoRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = serializers.VideoSerializer
    queryset = Video.objects.all()
    lookup_field = 'videoID'

    def get_queryset(self):
        return self.queryset


# FilmPurchase
class FilmPurchaseView(generics.CreateAPIView):
    serializer_class = serializers.FilmPurchaseSerializer

    def get_queryset(self):
        return FilmPurchase.objects.all()