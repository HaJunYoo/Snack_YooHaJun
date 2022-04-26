from django.db import models

from django.utils import timezone

class Snacks(models.Model):
    snackname = models.CharField(max_length=50)
    snackbrand = models.CharField(max_length=100)
    snackprice = models.IntegerField(default=0)
    producer = models.CharField(max_length=100)
    stockunit = models.CharField(max_length=10)
    qty = models.PositiveIntegerField(default=0)

    #
    def __str__(self):
        return f'{self.pk} : {self.snackname}'

