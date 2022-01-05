from django.db import models
from django.core.validators import EmailValidator, RegexValidator

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