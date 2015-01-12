# -*- coding: utf-8 -*-
from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    available_days = models.IntegerField( default = 0)
    balance = models.FloatField(default = 0.0)
    rechargetime = models.DateTimeField(default=datetime.datetime.now())
    def __unicode__(self):
        return self.username

class GlobVar(models.Model):
    autosubavday = models.BooleanField(default=False)
    currentfg = models.BooleanField(default=False)
    def __unicode__(self):
        return unicode(self.autosubavday) + unicode(self.currentfg)
