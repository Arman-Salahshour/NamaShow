from rest_framework import serializers
from Core.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('postID',)


class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('postID',)