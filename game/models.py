from django.db import models
import datetime


class Username(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True, default=None)
    date = models.DateTimeField(default=datetime.datetime.now)
    user_score = models.IntegerField(default=0)
    comp_score = models.IntegerField(default=0)
    hard_count = models.IntegerField(default=0)
    comments = models.TextField(max_length=1000, blank=True, null=True, default=None)

    def __str__(self):
        return ('%s') % self.username




    
