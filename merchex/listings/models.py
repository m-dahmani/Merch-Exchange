from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    # like_new = models.fields.BooleanField(default=False) <-- SUPPRIMER CETTE LIGNE second stratégy

    def __str__(self):
        # return f'{self.__class__.__name__} object ({self.id}) ({self.name})'
        return f'{self.name}'


class Listing(models.Model):

    TYPE_CHOICES = [
        ('Records', 'Records'),
        ('Clothing', 'Clothing'),
        ('Posters', 'Posters'),
        ('Miscellaneous', 'Miscellaneous'),
    ]

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    year = models.fields.IntegerField(null=True, blank=True)
    sold = models.fields.BooleanField(default=False)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default='Records')
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'
