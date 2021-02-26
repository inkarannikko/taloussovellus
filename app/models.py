from django.db import models
from django.db import connection


class Account(models.Model):
    date = models.DateTimeField()
    amount = models.FloatField()
    receiver = models.TextField()



