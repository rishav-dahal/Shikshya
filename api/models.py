from django.db import models

from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Role(models.Model):
    role_id=models.AutoField(primary_key=True)
    role =models.CharField(max_length=100)
    
class User(models.Model):
    u_id= models.BigAutoField(primary_key=True)
    role= models.ForeignKey(Role , on_delete=models.CASCADE)
    u_name= models.CharField(max_length=100)
    u_email = models.EmailField(max_length=100, unique=True)

class File(models.Model):
    file_id=models.BigAutoField(primary_key=True)
    file = models.FileField(upload_to='audio/')

class Content(models.Model):
    content_id=models.BigAutoField(primary_key=True)
    content_jason=models.JSONField()
    file=models.ForeignKey(File , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Class(models.Model):
    class_id=models.BigAutoField(primary_key=True)
    subject_name=models.CharField(max_length=250)
    semister= models.CharField(max_length=100)
