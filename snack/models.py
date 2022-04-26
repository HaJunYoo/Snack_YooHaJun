from django.db import models

from django.utils import timezone

class Snacks(models.Model):
    snackname = models.CharField(max_length=50)
    snackbrand = models.CharField(max_length=100)
    snackprice = models.IntegerField(default=0)
    producer = models.CharField(max_length=100)
    stockunit = models.CharField(max_length=10)
    qty = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=100)


    def status_check(self):
        return self.qty >= 1

    #
    def __str__(self):
        return f'{self.pk} : {self.snackname}'

