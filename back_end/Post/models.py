from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    adminID = models.PositiveIntegerField()
    textOf = models.TextField()
    dateOf = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0),])