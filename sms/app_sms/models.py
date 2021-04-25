from django.db import models

class SMS(models.Model):
    name = models.CharField(max_length=10)
    item = models.CharField(max_length=20)
    price = models.IntegerField()
    phone = models.CharField(max_length=20)
