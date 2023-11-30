from django.db import models

from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser, BaseUserManager

class  users(models.Model):
    uid= models.BigAutoField(primary_key=true)
    uname= models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
   

    REQUIRED_FIELDS = ["uname", "email"]

