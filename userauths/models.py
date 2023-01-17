from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    
    #set user name field to pick the email parameter
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username



