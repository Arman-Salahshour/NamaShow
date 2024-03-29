from rest_framework import serializers
from Core.models import Celebrity, Genre, Film


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


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('filmID', 'title', 'price', 'seasons', 'duration',
                  'statusOf', 'typeOf', 'numberOfFilminoRatings', 'filminoRating',
                  'rating', 'releaseDate', 'details', 'salePercentage', 'saleExpiration',)
        read_only_fields = ('filmID',)


# class VideoSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Celebrity
#         fields = ('videoID', 'duration', 'qualityHeight', 'qualityWidth', 'sizeOf',
#                   'episode', 'season', 'encoder', 'directoryLocation')
#         read_only_fields = ('celebID',)