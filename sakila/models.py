from datetime import date
from django.db import models

# Create your models here.
class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    last_update = models.DateField()
    
    class Meta:
        db_table = 'country'

    def __str__(self):
        return self.country
    

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_update = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = 'actor'

class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    actors = models.ManyToManyField('Actor', through='FilmActor')
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'film'
        
class FilmActor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'film_actor'
        unique_together = ('film', 'actor')
        managed = False
