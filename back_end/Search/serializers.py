from .models import Film
from rest_framework import serializers

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = [
            "filmID",
            "title",
            "price",
            "seasons",
            "duration",
            "statusOf",
            "typeOf",
            "numberOfFilminoRatings",
            "filminoRating",
            "rating",
            "releaseDate",
            "details",
            "salePercentage",
            "saleExpiration",
        ]