from django.db import models
from datetime import datetime 
class location(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=999)
    last_updated =  models.DateTimeField(default=datetime.now(), blank=True)   
    validate = models.CharField(max_length=999,default="Not yet Validated")
    def __str__(self):
        return self.name
    
class scrapper(models.Model):
    last_updated =  models.DateTimeField(default=datetime.now(), blank=True)   