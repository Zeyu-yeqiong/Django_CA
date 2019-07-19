from django.db import models
from django.conf import settings

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()




class RestaurantInfo(models.Model):
    name= models.CharField(max_length=32)
    picture= models.CharField(max_length=32)
    description= models.CharField(max_length=32)
    category= models.CharField(max_length=5)
    star= models.CharField(max_length=5)
    review_number=models.CharField(max_length=5)



class Review(models.Model):
    res_id=models.CharField(max_length=32)
    name= models.CharField(max_length=32)
    scontent=models.CharField(max_length=32)
    content= models.CharField(max_length=32)
    start=models.CharField(max_length=5)
    time=models.CharField(max_length=32)
    is_sub=models.CharField(max_length=32)
    subid=models.IntegerField()
    
