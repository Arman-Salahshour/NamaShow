from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import EmailValidator, RegexValidator, MaxValueValidator, MinValueValidator

# Create your models here.


class UserManager(BaseUserManager):
    def createUser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email Not Found!!!')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def createSuperUser(self, email, password):
        user = self.createUser(email, password)
        user.isAdmin = True
        user.isSuperUser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, validators=[RegexValidator(regex="^(?=[a-z0-9._]{5,20}$)(?!.*[_.]{2})[^_.].*[^_.]$")])
    email= models.EmailField(max_length=100, unique=True,  validators=[EmailValidator()])
    name = models.CharField(max_length=100)
    isSuspended = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
    emailActivation = models.BooleanField(default=False)
    balance = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'username'


class Sale(models.Model):
    saleID = models.AutoField(primary_key=True)
    typeOf = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(0),])
    salePercentage = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0),])
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()


class Celebrity(models.Model):
    celebID = models.AutoField(primary_key=True)
    nameOf = models.CharField(max_length=255)
    gender = models.BooleanField()
    dateOfBirth = models.DateField(null=True)
    nationality = models.CharField(null=True, max_length=255)
    
    def __str__(self):
        return self.nameOf


class Genre(models.Model):
    genreID = models.AutoField(primary_key=True)
    nameOf = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    
    def __str__(self):
        return self.nameOf


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
    photoDirectory = models.TextField()
    
    filmGenre = models.ManyToManyField(Genre)
    filmActor = models.ManyToManyField(Celebrity, related_name='actor')
    filmDirector = models.ManyToManyField(Celebrity, related_name='director')
    filmProducer = models.ManyToManyField(Celebrity, related_name='producer')

    def __str__(self):
        return f"{self.title} {self.releaseDate.strftime('%Y')}"


class Video(models.Model):
    videoID = models.AutoField(primary_key=True)
    duration = models.PositiveIntegerField()
    qualityHeight = models.PositiveIntegerField()
    qualityWidth = models.PositiveIntegerField()
    sizeOf = models.PositiveIntegerField()
    episode = models.PositiveIntegerField(default= 1)
    season = models.PositiveIntegerField(default= 1)
    encoder = models.CharField(max_length=30)
    directoryLocation = models.TextField()
    
    film = models.ForeignKey(Film, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.film}: s{self.season}e{self.episode}_{self.qualityWidth}p_{self.encoder}_{self.sizeOf}mB"


class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    textOf = models.TextField()
    dateOf = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0),])
    
    film = models.ForeignKey(Film, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class FilmPurchase(models.Model):
    price = models.PositiveIntegerField()
    dateOf = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    film = models.ForeignKey(Film, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.user}: {self.film}, {self.price}IRR, {self.dateOf}"


class Subscription(models.Model):
    subID = models.AutoField(primary_key=True)
    nameOf = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
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


class Payment(models.Model):
    trackingCode = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField()
    dateOf = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    # def __str__(self):
    #     return f"{self.user}: {self.amount}IRR, {self.trackingCode}"


class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    adminID = models.PositiveIntegerField()
    textOf = models.TextField()
    dateOf = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0),])