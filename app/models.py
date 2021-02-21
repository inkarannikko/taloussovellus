from django.db import models

class Account(models.Model):
    date = models.DateTimeField()
    receiver = models.TextField()
    amount = models.FloatField()


