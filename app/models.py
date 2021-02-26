from django.db import models

class Account(models.Model):
    date = models.DateTimeField()
    amount = models.FloatField()
    receiver = models.TextField()


