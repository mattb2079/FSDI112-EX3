from django.db import models

# Create the models here.


class Book (models.Model):
    title = models.CharField(max_length = 255)
    genre = models.CharField(max_length = 255)
    price = models.FloatField()


class Customer (models.Model):
    name = models.CharField(max_length = 255)
    number = models.IntegerField()
    address = models.CharField(max_length = 255)
