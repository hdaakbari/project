from django.db import models
from django.utils.text import slugify
from accounts.models import UserProfile
from django.urls import reverse,reverse_lazy

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=300,blank=True)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    like=models.ManyToManyField(UserProfile,related_name='post_like',null=True,blank=True)
    dislike=models.ManyToManyField(UserProfile,related_name='post_dislike',null=True,blank=True)

    def save(self,*args,**kwargs ):
        super().save()
        if not self.slug:
            self.slug = slugify(self.title)
            self.save()

    def get_absolute_url(self):
        return reverse("Post", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.body + "" + str(self.id)
    

class Comment(models.Model):
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE) #if post was deleted comment will deleted
    body=models.TextField()
    is_validate=models.BooleanField()
    created_at=models.DateTimeField(auto_now=True)
    update_at=models.DateTimeField(auto_now=True)

    def __st__(self):
        return self.created_at 
    
