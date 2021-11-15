from django.core import validators
from django.db import models
from django.core.validators import EmailValidator, MaxValueValidator, MinValueValidator, RegexValidator

# Create your models here.

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, validators=[RegexValidator(regex="^(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$")])
    email= models.CharField(max_length=100, unique=True,  validators=[EmailValidator()])
    password = models.TextField()
    emailActivation = models.BooleanField(default=False)
    nameOf = models.CharField(max_length=100)
    balance = models.PositiveIntegerField()

    def __str__(self):
        return self.username

    
class Payment(models.Model):
    trackingCode = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    dateOf = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.userID}: {self.amount}IRR, {self.trackingCode}"


class Subscription(models.Model):
    subID = models.AutoField(primary_key=True)
    nameOf = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    saleStatus = models.BooleanField(default=False)
    salePercentage = models.PositiveIntegerField(default=0)
    saleExpiration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nameOf}: {self.price}IRR"


class SubPurchase(models.Model):
    price = models.PositiveIntegerField()
    dateOf = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    subscription = models.ForeignKey(Subscription, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.subscription


class Movie(models.Model):
    movieID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0),])
    releaseDate = models.DateTimeField(null=True)
    details = models.TextField()
    saleStatus = models.BooleanField(default=False)
    salePercentage = models.PositiveIntegerField(default=0)
    saleExpiration = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class TVShow(models.Model):
    showID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    seasons = models.IntegerField(default=1)
    duration = models.PositiveIntegerField()
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0),])
    releaseDate = models.DateTimeField(null=True)
    showStatus = models.IntegerField(default=1, validators=[MaxValueValidator(4), MinValueValidator(1),])
    details = models.TextField()
    saleStatus = models.BooleanField(default=False)
    salePercentage = models.PositiveIntegerField(default=0)
    saleExpiration = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Film(models.Model):
    filmID = models.AutoField(primary_key=True)
    saleStatus = models.BooleanField(default=False)
    salePercentage = models.PositiveIntegerField(default=0)
    saleExpiration = models.DateTimeField(auto_now_add=True)

    movie = models.ForeignKey(Movie, blank=True, on_delete=models.CASCADE)
    tvshow = models.ForeignKey(TVShow, blank=True, on_delete=models.CASCADE)
    
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
    url = models.TextField
    
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