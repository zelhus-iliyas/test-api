from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     pass
class Ancestor(models.Model):
    _id = models.CharField(null=True, max_length=100)     
    speed = models.FloatField()
    heading = models.FloatField()
    altitude = models.FloatField()
    accuracy = models.FloatField()
    longitude = models.FloatField()
    altitudeAccuracy = models.FloatField(null=True)
    latitude = models.FloatField()
    mocked = models.BooleanField()
    timestamp = models.FloatField()
    _v = models.IntegerField(null=True)
    createdAt = models.CharField(null=True, max_length=100)
    updatedAt = models.CharField(null=True, max_length=100)
class NewJsonData(models.Model):
    newJsonData_id=models.AutoField(primary_key=True)
    speed = models.FloatField()
    heading = models.FloatField()
    altitude = models.FloatField()
    accuracy = models.FloatField()
    longitude = models.FloatField()
    altitudeAccuracy = models.FloatField(null=True)
    latitude = models.FloatField()
    
    pass

class NewApiJsonData(models.Model):
    
    newApiJsonData_id=models.AutoField(primary_key=True)
    _id = models.CharField(null=True, max_length=100)
    coords = models.ForeignKey(
        NewJsonData, on_delete=models.CASCADE,related_name='coords_ids', null=True, blank=True)
    mocked = models.BooleanField()
    timestamp = models.FloatField()
    _v = models.IntegerField(null=True)
    createdAt = models.CharField(null=True, max_length=100)
    updatedAt = models.CharField(null=True, max_length=100)

class Combined(NewJsonData,NewApiJsonData):
    pass

