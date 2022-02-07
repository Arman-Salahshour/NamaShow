from pyexpat import model
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from rest_framework import serializers
from Core.models import Celebrity, FilmPurchase, Genre, Film, Review, Video
from Core.OMDBcrawler import search_omdb
from datetime import datetime
from django.contrib.auth.models import AnonymousUser


# Genre serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genreID', 'nameOf', 'details')
        read_only_fields = ('genreID',)


# Genre Retrieve Serializer
class GenreRetrieveSerializer(serializers.ModelSerializer):
    class GenreFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Film
            fields = ('filmID', 'title', 'rating', 'posterDirectory', 'posterURL')
            read_only_fields = ('filmID', 'title', 'rating', 'posterDirectory', 'posterURL')
    
    film_set = GenreFilmSerializer(read_only=True, many=True,)
    class Meta:
        model = Genre
        fields = '__all__'


# Celebrity serializer
class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ('celebID', 'nameOf', 'gender', 'dateOfBirth', 'nationality')
        read_only_fields = ('celebID',)


# Celebrity Retrieve Serializer
class CelebrityRetrieveSerializer(serializers.ModelSerializer):
    class FilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Film
            fields = ('filmID', 'title', 'rating', 'posterDirectory', 'posterURL',)
            read_only_fields = ('filmID', 'title', 'rating', 'posterDirectory', 'posterURL')
    
    film_actor = FilmSerializer(read_only=True, many=True,)
    film_director = FilmSerializer(read_only=True, many=True,)
    class Meta:
        model = Celebrity
        fields = '__all__'


# Film
# Film Listing view serializer
class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('filmID', 'title', 'rating', 'posterDirectory', 'posterURL')
        read_only_fields = ('filmID', 'title', 'rating', 'posterDirectory', 'posterURL')


# Film create view serializer
class FilmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        read_only_fields = ('filmID', 'duration', 'rating', 'releaseDate', 'posterDirectory', 'posterURL', 'typeOf', 'isAnimation', 'salePercentage',
                            'filmGenre', 'filmActor', 'filmDirector', 'filminoRating', 'numberOfFilminoRatings', 'detailsEn')

    def create(self, validated_data):
        title = validated_data['title']
        data = search_omdb(title)

        if data['Response'] != 'True':
            raise BaseException('Can not find this film in the database')

        #Title
        validated_data['title'] = data['Title'] + ' ' + data['Year'][:4]
        
        #Release Date
        dateString = data['Released'] + ' 12:00 AM'
        releaseDate = datetime.strptime(dateString, '%d %b %Y %I:%M %p')
        validated_data['releaseDate'] = releaseDate
        
        #Duration
        runtime = data['Runtime']
        numbers = []
        for word in runtime.split():
            if word.isdigit():
                numbers.append(int(word))
        duration = int(numbers[0])
        validated_data['duration'] = duration

        #Rating
        rating = data['Ratings'][0]['Value']
        rating = rating[0:3]
        validated_data['rating'] = float(rating)

        #Photo Directory
        if data['Poster']!='N/A':
            validated_data['posterURL'] = data['Poster']
            validated_data['posterDirectory'] = data['PosterLoc'].split('\\')[-1]

        #Details
        if data['Plot']!='N/A':
            validated_data['detailsEn'] = data['Plot'] 

        #Type
        if data['Type']!='N/A':
            if(data['Type']=='movie'):
                validated_data['typeOf'] = 1
            elif(data['Type']=='series'):
                validated_data['typeOf'] = 2
            else:
                validated_data['typeOf'] = 3
        else:
            validated_data['typeOf'] = 3


        #Genres
        if data['Genre']!='N/A':
            genre_list = data['Genre'].split(', ')
            genres = []
            for loopgenre in genre_list:
                if not Genre.objects.filter(nameOf=loopgenre):
                    Genre.objects.create(nameOf=loopgenre)
                newGenre = Genre.objects.get(nameOf=loopgenre)
                genres.append(newGenre)
            validated_data['filmGenre'] = genres

        
        #IsAnimation
        if('Animation' in genre_list):
            validated_data['isAnimation'] = True
        else:
            validated_data['isAnimation'] = False


        #Actors
        if data['Actors']!='N/A':
            actor_list = data['Actors'].split(', ')
            actors = []
            for loopactor in actor_list:
                if not Celebrity.objects.filter(nameOf=loopactor):
                    Celebrity.objects.create(nameOf=loopactor)
                newActor = Celebrity.objects.get(nameOf=loopactor)
                actors.append(newActor)
            validated_data['filmActor'] = actors

        #Directors
        if data['Director']!='N/A':
            director_list = data['Director'].split(', ')
            directors = []
            for loopdirector in director_list:
                if not Celebrity.objects.filter(nameOf=loopdirector):
                    Celebrity.objects.create(nameOf=loopdirector)
                newDirector = Celebrity.objects.get(nameOf=loopdirector)
                directors.append(newDirector)
            validated_data['filmDirector'] = directors


        return super().create(validated_data)


# Film retrieve serializer
class FilmRetrieveSerializer(serializers.ModelSerializer):
    class ReviewFilmSerialzier(serializers.ModelSerializer):
        class UserReviewFilmSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('userID', 'username', 'email')
                read_only_fields = ('userID', 'username', 'email')

        user = UserReviewFilmSerializer(read_only=True)

        class Meta:
            model = Review
            fields = ('reviewID', 'textOf', 'rating', 'user')
            read_only_fields = ('reviewID', 'textOf', 'rating', 'user')

    class GenreFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('nameOf', 'genreID',)
            read_only_fields = ('nameOf', 'genreID',)
        
        def to_representation(self, instance):
            ret = super().to_representation(instance)
            ret = {'name': ret['nameOf'], 'id': ret['genreID']}
            return ret

    class CelebrityFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Celebrity
            fields = ('nameOf', 'celebID',)
            read_only_fields = ('nameOf', 'celebID',)
        
        def to_representation(self, instance):
            ret = super().to_representation(instance)
            ret = {'name': ret['nameOf'], 'id': ret['celebID']}
            return ret


    class VideoFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Video
            fields = '__all__'

    filmGenre = GenreFilmSerializer(read_only=True, many=True)
    filmActor = CelebrityFilmSerializer(read_only=True, many=True)
    filmDirector = CelebrityFilmSerializer(read_only=True, many=True)
    videoDetails = VideoFilmSerializer(read_only=True, many=True, source='video_set')
    reviews = ReviewFilmSerialzier(read_only=True, many=True, source='review_set')

    class Meta:
        model = Film
        fields = ('filmID', 'title', 'price', 'duration',
                  'typeOf', 'numberOfFilminoRatings', 'filminoRating',
                  'rating', 'releaseDate', 'detailsEn', 'detailsFa', 'salePercentage', 'saleExpiration', 'posterDirectory',
                  'posterURL', 'filmGenre', 'filmActor', 'filmDirector', 'videoDetails', 'reviews')
        read_only_fields = ('filmID',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['user_purchased'] = False
        ret['user_reviewed'] = False
        fID = ret['filmID']
        film = Film.objects.filter(filmID=fID).first()
        request = self.context.get("request")
        user = request.user
        if(type(user) != AnonymousUser):
            if(FilmPurchase.objects.filter(user=user).filter(film=film).first()):
                ret['user_purchased'] = True
            review = Review.objects.filter(user=user).filter(film=film).first()
            if(review):
                ret['user_reviewed'] = True
                ret['user_review_id'] = int(getattr(review, 'reviewID'))
        return ret


# Video Serializer
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('videoID', 'film', 'duration', 'qualityHeight', 'qualityWidth', 'sizeOf',
                  'episode', 'season', 'encoder', 'directoryLocation')
        read_only_fields = ('videoID',)


# FilmPurchase serializer
class FilmPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPurchase
        fields = ('user', 'film', 'price','dateOf')
        read_only_fields = ('user', 'price', 'dateOf')

    def create(self, validated_data):
        validated_data['dateOf'] = datetime.now()

        request = self.context.get("request")
        user = request.user
        validated_data['user'] = user
        uID = getattr(user,'userID')

        film = validated_data['film']
        if(FilmPurchase.objects.filter(user=user).filter(film=film).first()):
            raise ValidationError('Already Own This Film.', code='repurchase')

        price = int(getattr(film,'price'))
        validated_data['price'] = price
        balance = int(getattr(user, 'balance'))
        if(price>balance):
            raise ValidationError('Not enough balance.', code='low_balance')
        balance = balance - price
        get_user_model().objects.filter(userID=uID).update(balance=balance)        

        return super().create(validated_data)


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('reviewID', 'textOf', 'rating', 'user', 'film')
        read_only_fields = ('reviewID', 'user')
        extra_kwargs = {'rating': {'min_value': 0, 'max_value': 10}}
    
    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data['user'] = user
        film = validated_data['film']
        fID = getattr(film,'filmID')
        prevRev = Review.objects.filter(user=user).filter(film=film).first()
        if(prevRev):
            raise ValidationError('Already have a review on this film.', code='rereview')
        fRating = int(getattr(film,'filminoRating'))
        fNumbers = int(getattr(film, 'numberOfFilminoRatings'))
        total = fRating * fNumbers
        fNumbers = fNumbers + 1
        fRating = (total + int(validated_data['rating'])) / fNumbers
        fID = getattr(film,'filmID')
        Film.objects.filter(filmID=fID).update(filminoRating=fRating)
        Film.objects.filter(filmID=fID).update(numberOfFilminoRatings=fNumbers)
        return super().create(validated_data)


class ReviewRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'