from xmlrpc.client import MAXINT, MININT
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class MyWatchList(models.Model):
    watched =  models.BooleanField()
    title = models.TextField()
    rating =  models.IntegerField()
    release_date =  models.TextField()
    review =  models.TextField()
    