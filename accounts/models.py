from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    bio=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='profile_picture')
    
class Education(models.Model):
    school=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    fos=models.CharField(max_length=100)
    start=models.DateTimeField()
    end=models.TextField()
    desc=models.TextField()
    
class Experience(models.Model):
    title=models.CharField(max_length=100)
    compony=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    start=models.DateTimeField()
    end=models.DateField()
    description=models.TextField()
    