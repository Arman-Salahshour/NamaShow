from isodate import duration_isoformat
from rest_framework import serializers
from Core.models import Celebrity, Genre, Film, Video
from Core.OMDBcrawler import search_omdb
from datetime import datetime


# Genre serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genreID', 'nameOf', 'details')
        read_only_fields = ('genreID',)


# Celebrity serializer
class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ('celebID', 'nameOf', 'gender', 'dateOfBirth', 'nationality')
        read_only_fields = ('celebID',)


# Film
# Film Listing view serializer
class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('filmID', 'title', 'rating',)
        read_only_fields = ('filmID', 'title', 'rating',)


# Film create view serializer
class FilmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        read_only_fields = ('filmID', 'duration', 'rating', 'releaseDate', 'photoDirectory', 'typeOf', 'salePercentage',
                            'filmGenre', 'filmActor', 'filmDirector', 'filminoRating', 'numberOfFilminoRatings')

    def create(self, validated_data):
        title = validated_data['title']
        data = search_omdb(title)

        if data['Response'] != 'True':
            raise BaseException('Can not find this film in the database')

        #Title
        validated_data['title'] = data['Title'] + ' ' + data['Year']
        
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
            validated_data['photoDirectory'] = data['PosterLoc'].split('\\')[-1]

        #Details
        if data['Plot']!='N/A':
            validated_data['details'] = 'English:\n' + data['Plot'] + '\nPersian:\n' + validated_data['details']  

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


# Film retrieve view serializer
class FilmRetrieveSerializer(serializers.ModelSerializer):
    class GenreFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('nameOf',)
            read_only_fields = ('nameOf',)
        
        def to_representation(self, instance):
            ret = super().to_representation(instance)
            ret = ret['nameOf'] 
            return ret

    class CelebrityFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Celebrity
            fields = ('nameOf',)
            read_only_fields = ('nameOf',)
        
        def to_representation(self, instance):
            ret = super().to_representation(instance)
            ret = ret['nameOf'] 
            return ret

    class VideoFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model = Video
            fields = '__all__'

    filmGenre = GenreFilmSerializer(read_only=True, many=True)
    filmActor = CelebrityFilmSerializer(read_only=True, many=True)
    filmDirector = CelebrityFilmSerializer(read_only=True, many=True)
    videoDetails = VideoFilmSerializer(read_only=True, many=True, source='video_set')
    class Meta:
        model = Film
        fields = ('filmID', 'title', 'price', 'duration',
                  'typeOf', 'numberOfFilminoRatings', 'filminoRating',
                  'rating', 'releaseDate', 'details', 'salePercentage', 'saleExpiration', 'photoDirectory',
                  'filmGenre', 'filmActor', 'filmDirector', 'videoDetails')
        read_only_fields = ('filmID',)


# Video Serializer
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('videoID', 'film', 'duration', 'qualityHeight', 'qualityWidth', 'sizeOf',
                  'episode', 'season', 'encoder', 'directoryLocation')
        read_only_fields = ('videoID',)