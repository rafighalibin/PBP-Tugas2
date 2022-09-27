from datetime import datetime, timezone
from turtle import title
from xmlrpc.client import MAXINT, MININT
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Task(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)
    title =  models.TextField()
    desc =  models.TextField()
    is_finished  = models.BooleanField(default=False)
    