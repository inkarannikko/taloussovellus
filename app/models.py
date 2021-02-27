from django.db import models
from django.db import connection


class Account(models.Model):
    date = models.DateTimeField()
    amount = models.FloatField()
    receiver = models.TextField()

@property
def __get__year(self):
    return self.date.strftime("%Y-%m" )

    year = property(__get_year)
