from django.db import models
from Login.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Film(models.Model):
    filmID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    seasons = models.IntegerField(default=1)
    duration = models.PositiveIntegerField()
    statusOf = models.IntegerField(default=1, validators=[MaxValueValidator(4), MinValueValidator(1),])
    typeOf = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1),])
    numberOfFilminoRatings = models.PositiveIntegerField(default=0)
    filminoRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0),])
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0),])
    releaseDate = models.DateTimeField(null=True)
    details = models.TextField()
    salePercentage = models.PositiveIntegerField(default=0)
    saleExpiration = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.movie}{self.tvshow}"


class Video(models.Model):
    videoID = models.AutoField(primary_key=True)
    duration = models.PositiveIntegerField()
    qualityHeight = models.PositiveIntegerField()
    qualityWidth = models.PositiveIntegerField()
    sizeOf = models.PositiveIntegerField()
    episode = models.PositiveIntegerField()
    season = models.PositiveIntegerField()
    encoder = models.CharField(max_length=20)
    directoryLocation = models.TextField()
    
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.film}: s{self.season}e{self.episode} {self.qualityWidth} {self.encoder} {self.sizeOf}mB"


class Celebrity(models.Model):
    celebID = models.AutoField(primary_key=True)
    nameOf = models.CharField(max_length=150)
    gender = models.BooleanField()
    dateOfBirth = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.nameOf


class Genre(models.Model):
    genreID = models.AutoField(primary_key=True)
    nameOf = models.CharField(max_length=150)
    details = models.TextField()
    
    def __str__(self):
        return self.nameOf


class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    filmID = models.PositiveIntegerField()
    userID = models.PositiveIntegerField()
    textOf = models.TextField()
    dateOf = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0),])


class FilmPurchase(models.Model):
    price = models.PositiveIntegerField()
    dateOf = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    film = models.ForeignKey(Film, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.user}: {self.film}, {self.price}IRR, {self.dateOf}"


class FilmGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class FilmActor(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class FilmDirector(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class FilmProducer(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)