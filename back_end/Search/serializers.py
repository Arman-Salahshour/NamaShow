from Core.models import Film
from rest_framework import serializers

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = [
            "filmID", "title", "price", "duration", "typeOf", "numberOfFilminoRatings",
            "filminoRating", "rating", "releaseDate", "detailsEn", "salePercentage",
            "saleExpiration", "posterURL", "posterDirectory", 'isAnimation'
        ]