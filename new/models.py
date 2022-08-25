from django.utils.timezone import now
from django.db import models


class NewJson(models.Model):
    _id = models.CharField(null=True, max_length=100)
    created_date = models.DateTimeField(default=now,editable=False)
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
    
    def __str__(self):
        return self._id