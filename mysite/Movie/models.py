from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Movie(models.Model):
    name = models.CharField('Name', max_length=100, unique=True)
    description = models.TextField('Description', null=True, blank=True)
    genre = models.ForeignKey('Genre')
    director = models.ForeignKey('Director')
    year = models.IntegerField('Year of release', null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Genre', max_length=50, unique=True)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField('Director name', max_length=50, unique=True)
    year = models.IntegerField('Year of birth', null=True)
    nationality = models.CharField("Nationality", max_length=100)
    height = models.FloatField("Height")

    def __str__(self):
        return self.name
