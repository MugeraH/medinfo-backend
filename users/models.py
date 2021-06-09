from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=250, unique=True)
    firstname = models.CharField(max_length=255,null=True)
    lastname = models.CharField(max_length=255,null=True)
    
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []
    