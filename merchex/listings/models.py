from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        COUPE_DECALE = 'CD'
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)

    def __str__(self): #au lieu d'afficher « Band object (id number)» affichons le nom du groupe
        return f'{self.name}'


class Song(models.Model):
    title = models.fields.CharField(max_length=100)

class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)], blank=True)
    
    class Type(models.TextChoices):
        RECORDS = 'RCD'
        CLOTHING = 'CLT'
        POSTERS = 'PTR'
        MISCELLANEOUS ='MLS'

    def __str__(self):
        return f'{self.description}'
    type = models.fields.CharField(choices=Type.choices, max_length=5)

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

