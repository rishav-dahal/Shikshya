from django.db import models

from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(models.Model):
    u_id= models.BigAutoField(primary_key=True)
    role_id= models.IntegerField(foreign_key=True)
    uname= models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    role_id=models.AutoField(primary_key=True)
    role =models.CharField(max_length=100)

class Content(models.Model):
    content_id=models.BigAutoField(primary_key=True)
    content_jason=models.JSONField()
    file_id=models.IntegerField(foreign_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

class File(models.Model):
    file_id=models.BigAutoField(primary_key=True)
    path=models.CharField(max_length=250)

class Class(models.Model):
    class_id=models.BigAutoField(primary_key=True)
    subject_name=models.CharField(max_length=250)
    semister= models.CharField(max_length=100)
