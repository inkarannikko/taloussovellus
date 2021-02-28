from django.db import models
from django.db import connection


class Account(models.Model):
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=5,decimal_places=2)
    receiver = models.TextField()
