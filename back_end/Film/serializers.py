from rest_framework import serializers
from Core.models import Celebrity, Genre, Film, Video


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genreID', 'nameOf', 'details')
        read_only_fields = ('genreID',)


class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ('celebID', 'nameOf', 'gender', 'dateOfBirth', 'nationality')
        read_only_fields = ('celebID',)


class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('filmID', 'title', 'rating',)
        read_only_fields = ('filmID', 'title', 'rating',)


class FilmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('filmID', 'title', 'price', 'seasons', 'duration',
                  'statusOf', 'typeOf', 'numberOfFilminoRatings', 'filminoRating',
                  'rating', 'releaseDate', 'details', 'salePercentage', 'saleExpiration',
                  'filmGenre', 'filmActor', 'filmDirector', 'filmProducer')
        read_only_fields = ('filmID',)


class FilmRetrieveSerializer(serializers.ModelSerializer):
    class GenreFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('nameOf',)
            # read_only_fields = ('nameOf',)
        
        def to_representation(self, instance):
            """Convert `username` to lowercase."""
            ret = super().to_representation(instance)
            ret = ret['nameOf'] 
            return ret

    class CelebrityFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Celebrity
            fields = ('nameOf',)
            read_only_fields = ('nameOf',)
        
        def to_representation(self, instance):
            """Convert `username` to lowercase."""
            ret = super().to_representation(instance)
            ret = ret['nameOf'] 
            return ret

    filmGenre = GenreFilmSerializer(read_only=True, many=True)
    filmActor = CelebrityFilmSerializer(read_only=True, many=True)
    filmDirector = CelebrityFilmSerializer(read_only=True, many=True)
    filmProducer = CelebrityFilmSerializer(read_only=True, many=True)
    class Meta:
        model = Film
        fields = ('filmID', 'title', 'price', 'seasons', 'duration',
                  'statusOf', 'typeOf', 'numberOfFilminoRatings', 'filminoRating',
                  'rating', 'releaseDate', 'details', 'salePercentage', 'saleExpiration',
                  'filmGenre', 'filmActor', 'filmDirector', 'filmProducer')
        read_only_fields = ('filmID',)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('videoID', 'film', 'duration', 'qualityHeight', 'qualityWidth', 'sizeOf',
                  'episode', 'season', 'encoder', 'directoryLocation')
        read_only_fields = ('videoID',)