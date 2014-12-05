# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    available_days = models.IntegerField( default = 0)
    balance = models.FloatField(default = 0.0)

    def __unicode__(self):
        return self.username;
