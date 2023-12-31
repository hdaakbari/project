from django.urls import reverse,reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.db import models
from django.contrib.auth.models import User
#from .models import UserProfile

# Create your models here.
class UserProfile(models.Model):
    bio=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='profile_picture', default="default_profile_picture.png")

    def get_absolute_url(self):
        return reverse_lazy("profile", args=[self.pk])
    
    
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


@receiver(post_save,sender=User)
def create_userprofile(sender,instance,**kwargs):
    if UserProfile.objects.filter(user=instance).count()==0:
        UserProfile.objects.create(user=instance)
    