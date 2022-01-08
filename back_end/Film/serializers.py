from rest_framework import serializers
from Core.models import Celebrity, Genre


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


# class VideoSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Celebrity
#         fields = ('videoID', 'duration', 'qualityHeight', 'qualityWidth', 'sizeOf',
#                   'episode', 'season', 'encoder', 'directoryLocation')
#         read_only_fields = ('celebID',)